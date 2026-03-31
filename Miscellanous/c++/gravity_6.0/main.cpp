#include <iostream>
#include "gravity.hpp" // Everything main needs to know is in here

int main() {
    GravityCalculator sim(100.0);
    std::cout << "Height after 2 seconds: " << sim.get_position(2.0) << "m" << std::endl;
    return 0;
}





