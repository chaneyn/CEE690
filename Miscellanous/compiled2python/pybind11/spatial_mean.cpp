#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

double compute_mean(py::array_t<double> input_array) {
    // 1. Request a safe, 3-Dimensional proxy object from the array.
    // The <3> explicitly tells pybind11 we are expecting a 3D grid.
    auto grid = input_array.unchecked<3>(); 

    // Safety check
    if (input_array.size() == 0) {
        throw std::runtime_error("Cannot compute mean of an empty array.");
    }

    double sum = 0.0;

    // 2. Iterate using the proxy object's built-in shape() methods
    // NO pointers, NO pointer arithmetic, NO static casts.
    for (py::ssize_t i = 0; i < grid.shape(0); i++) {
        for (py::ssize_t j = 0; j < grid.shape(1); j++) {
            for (py::ssize_t k = 0; k < grid.shape(2); k++) {
                
                // 3. Access the data using standard mathematical coordinates
                sum += grid(i, j, k); 
                
            }
        }
    }

    return sum / input_array.size();
}

// 4. The Python Binding
PYBIND11_MODULE(spatial_math, m) {
    m.doc() = "C++ Spatial Math Engine (Pointer-Free)"; 
    m.def("compute_mean", &compute_mean, "Compute the spatial mean of a 3D NumPy array");
}


