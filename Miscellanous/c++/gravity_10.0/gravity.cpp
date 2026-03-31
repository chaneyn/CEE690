#include "gravity.hpp"

// Use the Scope Resolution Operator (::) to fulfill the promises
GravityCalculator::GravityCalculator(double h) {
    initial_height = h;
}

double GravityCalculator::get_position(double t) {
    return initial_height - (0.5 * g * t * t);
}



