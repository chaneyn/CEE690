#include <iostream>

int main() {
    // Attempting to use the class defined in the other file
    GravityCalculator sim(100.0);
    
    std::cout << "Height at 2 seconds: " << sim.get_position(2.0) << "m" << std::endl;
    
    return 0;
}



