// Notice: ZERO Python or pybind11 includes!

extern "C" {
    // We pass a flat double pointer and the total size of the grid
    double compute_mean(const double* array, long total_elements) {
        if (total_elements <= 0) return 0.0;

        double sum = 0.0;
        
        // Iterate over the flat memory block
        for (long i = 0; i < total_elements; i++) {
            sum += array[i];
        }

        return sum / total_elements;
    }
}


