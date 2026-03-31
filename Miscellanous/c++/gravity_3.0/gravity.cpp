#include <iostream>

// We don't need the whole class block here if we use the Scope Resolution Operator
// to define the specific functions
class GravityCalculator {
    double initial_height;
    double g = 9.81;
public:
    GravityCalculator(double h);
    double get_position(double t);
};

GravityCalculator::GravityCalculator(double h) {
    initial_height = h;
}

double GravityCalculator::get_position(double t) {
    return initial_height - (0.5 * g * t * t);
}



