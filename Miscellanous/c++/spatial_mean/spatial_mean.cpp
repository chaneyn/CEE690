#include <iostream>

int main() {
    // 1. Initialize a 3x3 grid for simplicity
    double grid[3][3] = {
        {10.2, 11.5, 9.8},
        {12.1, 10.0, 11.2},
        {9.5,  10.8, 11.1}
    };

    double sum = 0.0;
    int rows = 3;
    int cols = 3;

    // 2. Nested Loops: Row-major traversal
    for (int i = 0; i < rows; i++) {         // Outer loop (Rows)
        for (int j = 0; j < cols; j++) {     // Inner loop (Columns)
            sum += grid[i][j];               // Accumulate the values
        }
    }

    // 3. Calculate Mean
    // Note: total elements is rows * cols
    double mean = sum / (rows * cols);

    std::cout << "The spatial mean of the grid is: " << mean << std::endl;

    return 0;
}



