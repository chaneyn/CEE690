#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cstdlib> // For system() calls
#include <netcdf>
#include <nlohmann/json.hpp>
#include <unsupported/Eigen/CXX11/Tensor>

using json = nlohmann::json;
using namespace netCDF;
using namespace netCDF::exceptions;

class SpatialAnalyzer {
public:
    // Attributes
    json config;
    Eigen::Tensor<double, 3> data; 
    std::vector<double> means;
    std::vector<double> variances;

    // Constructor
    SpatialAnalyzer(json cfg) : config(cfg) {
        load_dataset();
    }

    // 1. Data Loading
    void load_dataset() {
        std::string input_file = config["INPUT_FILE"];
        
        std::cout << "Loading dataset: " << input_file << std::endl;
        
        // Validation (ifstream used here just to check if file exists!)
        std::ifstream f(input_file.c_str());
        if (!f.good()) {
            std::cerr << "Error: The file " << input_file << " does not exist." << std::endl;
            exit(1);
        }
        f.close();

        try {
            NcFile dataFile(input_file, NcFile::read);
            std::string var_name = config["VAR_NAME"];
            NcVar var = dataFile.getVar(var_name);
            
            auto dims = var.getDims(); // Should be Time, Lat, Lon
            int T = dims[0].getSize();
            int Y = dims[1].getSize();
            int X = dims[2].getSize();

            // Resize the Eigen Tensor and load data directly into its contiguous memory
            data.resize(T, Y, X);
            var.getVar(data.data());

        } catch (NcException& e) {
            std::cerr << "NetCDF Error: " << e.what() << std::endl;
            exit(1);
        }
    }

    // 2. Compute Statistics
    void run_analysis() {
        std::cout << "Computing the statistics..." << std::endl;

        int t_start = config["TIME_MIN"], t_end = config["TIME_MAX"];
        int lat_min = config["LAT_MIN"], lat_max = config["LAT_MAX"];
        int lon_min = config["LON_MIN"], lon_max = config["LON_MAX"];

        double n_spatial = (lat_max - lat_min) * (lon_max - lon_min);

        // HPC Engine: Manual loops using Eigen's (t, y, x) indexing
        for (int t = t_start; t < t_end; t++) {
            double sum = 0.0;
            double sq_sum = 0.0;

            for (int y = lat_min; y < lat_max; y++) {
                for (int x = lon_min; x < lon_max; x++) {
                    double val = data(t, y, x); 
                    sum += val;
                    sq_sum += (val * val);
                }
            }

            double mean = sum / n_spatial;
            double var = (sq_sum / n_spatial) - (mean * mean);
            
            means.push_back(mean);
            variances.push_back(var);
        }
    }

    // 3. Visualization (The C++ to Python Bridge)
    void visualize() {
        if (means.empty()) {
            std::cerr << "Error: No results to visualize." << std::endl;
            return;
        }

        std::cout << "Visualizing the data..." << std::endl;
        std::string plot_file = config["PLOT_FILE"];
        std::string var_name = config["VAR_NAME"];

        // Write the data to a temporary CSV
        std::ofstream csv("temp_plot_data.csv");
        csv << "TimeStep,Mean,Variance\n";
        for (size_t i = 0; i < means.size(); i++) {
            csv << i << "," << means[i] << "," << variances[i] << "\n";
        }
        csv.close();

        // Write a temporary Python script
        std::ofstream py("temp_plotter.py");
        py << "import matplotlib\n"
           << "matplotlib.use('Agg')\n"
           << "import matplotlib.pyplot as plt\n"
           << "import pandas as pd\n"
           << "df = pd.read_csv('temp_plot_data.csv')\n"
           << "plt.figure(figsize=(10, 6))\n"
           << "plt.plot(df['Mean'], label='Spatial Mean')\n"
           << "plt.plot(df['Variance'], label='Spatial Variance')\n"
           << "plt.title('Statistics for " << var_name << "')\n"
           << "plt.xlabel('Time Step')\n"
           << "plt.ylabel('Value')\n"
           << "plt.legend()\n"
           << "plt.savefig('" << plot_file << "')\n";
        py.close();

        // Run the script and clean up
        int result = system("python temp_plotter.py");
        if (result == 0) {
            std::cout << "Plot saved to " << plot_file << std::endl;
        } else {
            std::cerr << "Warning: Matplotlib plotting failed." << std::endl;
        }
        
        system("rm temp_plot_data.csv temp_plotter.py"); // Cleanup temp files
    }

    // 4. Export NetCDF
    void save_netcdf() {
        std::string out_file = config["OUTPUT_FILE"];
        std::cout << "Saving statistics to " << out_file << std::endl;

        try {
            NcFile dataFile(out_file, NcFile::replace);
            NcDim tDim = dataFile.addDim("t", means.size());
            
            NcVar mVar = dataFile.addVar("temporal_spatial_mean", ncFloat, tDim);
            NcVar vVar = dataFile.addVar("temporal_spatial_variance", ncFloat, tDim);

            mVar.putVar(means.data());
            vVar.putVar(variances.data());
        } catch (NcException& e) {
            std::cerr << "Error while saving NetCDF: " << e.what() << std::endl;
        }
    }
};

// --- Command Line & Config Parsing ---
json get_args(int argc, char* argv[]) {
    // 1. Establish Defaults
    json config = {
        {"INPUT_FILE", "era_interim_monthly_197901_201512_upscaled_annual.nc"},
        {"OUTPUT_FILE", "out.nc"},
        {"PLOT_FILE", "plot.png"},
        {"VAR_NAME", "t2m"},
        {"LAT_MIN", 5}, {"LAT_MAX", 50},
        {"LON_MIN", 10}, {"LON_MAX", 100},
        {"TIME_MIN", 0}, {"TIME_MAX", 10},
        {"JSON_FILE", ""}
    };

    // 2. Simple CLI Parser (Overrides defaults)
    for (int i = 1; i < argc; i++) {
        std::string arg = argv[i];
        if (arg == "--JSON_FILE" && i + 1 < argc) config["JSON_FILE"] = argv[++i];
        else if (arg == "--INPUT_FILE" && i + 1 < argc) config["INPUT_FILE"] = argv[++i];
        // Note: For a full script, you would add the rest of the --FLAGS here
    }

    // 3. JSON Overrides CLI if provided
    std::string json_path = config["JSON_FILE"];
    if (!json_path.empty()) {
        std::ifstream f(json_path);
        if (f.is_open()) {
            json file_config;
            f >> file_config;
            config.merge_patch(file_config); // Update defaults with JSON keys
            std::cout << "Configuration loaded from " << json_path << std::endl;
        } else {
            std::cerr << "Warning: JSON file not found." << std::endl;
        }
    }

    return config;
}

// --- Main Execution ---
int main(int argc, char* argv[]) {
    json config = get_args(argc, argv);

    SpatialAnalyzer analyzer(config);
    analyzer.run_analysis();
    analyzer.visualize();
    analyzer.save_netcdf();

    std::cout << "Processing complete." << std::endl;
    return 0;
}
