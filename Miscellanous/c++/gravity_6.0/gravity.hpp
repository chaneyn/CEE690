#pragma once

class GravityCalculator {
private:
    double initial_height;
    double g = 9.8;

public:
    // We only put the signatures (the promises) here
    GravityCalculator(double h);
    double get_position(double t);
};



