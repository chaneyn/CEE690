
#include <iostream>

int main() {
    // 1. Variable Declarations (The "Boxes" in memory)
    double y0 = 100.0;    // Initial height in meters
    double g = 9.81;      // Acceleration due to gravity
    double y;             // We will calculate this in the loop

    // 2. The Header Print
    std::cout << "Time(s) | Position(m)" << std::endl;
    std::cout << "--------------------" << std::endl;

    // 3. The Calculation Loop (0 to 5 seconds)
    for (int t = 0; t <= 2; t++) {

        // C++ Math: Note that we use 0.5 instead of 1/2
        // (In C++, 1/2 would be 0 because it's integer division!)
        y = y0 - (0.5 * g * t * t);

        // 4. Output the result
        std::cout << t << "       | " << y << std::endl;
    }

    return 0;
}



