#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <netcdf>
#include <ncException.h> // <-- Added modern exception header
#include <string>
#include <vector>
#include <stdexcept>

namespace py = pybind11;
using namespace netCDF;

// The function: Takes a filename and a variable name, returns a NumPy array
py::array_t<double> read_netcdf_2d(const std::string& filename, const std::string& var_name) {
    try {
        // 1. Open the file in read-only mode using the C++ API
        NcFile dataFile(filename, NcFile::read);
        
        // 2. Get the variable object
        NcVar var = dataFile.getVar(var_name);
        if (var.isNull()) {
            throw std::runtime_error("Variable '" + var_name + "' not found in file.");
        }
        
        // 3. Check dimensions (Ensure it's actually 2D)
        std::vector<NcDim> dims = var.getDims();
        if (dims.size() != 2) {
            throw std::runtime_error("This specific wrapper only handles 2D variables.");
        }
        
        size_t rows = dims[0].getSize();
        size_t cols = dims[1].getSize();
        
        // 4. Allocate the NumPy array in memory
        // We tell pybind11 the shape we need based on the NetCDF metadata
        py::array_t<double> result_array({rows, cols});
        
        // 5. THE MAGIC STEP: Direct Memory Read
        // We get a mutable pointer to the NumPy array's raw memory buffer
        // and tell the NetCDF library to read the disk data directly into it!
        var.getVar(result_array.mutable_data());
        
        return result_array;
        
    } catch (netCDF::exceptions::NcException& e) { // <-- Updated Conda namespace
        // Catch NetCDF specific C++ errors and pass them to Python
        throw std::runtime_error(std::string("NetCDF Error: ") + e.what());
    }
}

// 6. The pybind11 Module Definition
PYBIND11_MODULE(fast_nc, m) {
    m.doc() = "High-speed C++ NetCDF reader for Python";
    m.def("read_2d", &read_netcdf_2d, "Read a 2D double-precision variable directly into NumPy");
}
