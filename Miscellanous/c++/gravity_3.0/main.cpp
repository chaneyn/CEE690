#include <iostream>

// --- THE BRUTE FORCE FIX ---
// We copy the "Blueprint" (the class structure) into this file
// so the compiler knows how much memory to allocate for 'sim'
class GravityCalculator {
private:
    double initial_height;
    double g = 9.81;

public:
    GravityCalculator(double h);         // We "promise" this exists
    double get_position(double t);       // We "promise" this exists
};
// ----------------------------

int main() {
    // Now the compiler says: "Aha! I know what a GravityCalculator is!"
    GravityCalculator sim(100.0);
    
    std::cout << "Height at 2 seconds: " << sim.get_position(2.0) << "m" << std::endl;
    
    return 0;
}

