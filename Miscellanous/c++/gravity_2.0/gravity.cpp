#include <iostream>

class GravityCalculator {
private:
    double initial_height;
    double g = 9.81;

public:
    GravityCalculator(double h) {
        initial_height = h;
    }

    double get_position(double t) {
        return initial_height - (0.5 * g * t * t);
    }
};



