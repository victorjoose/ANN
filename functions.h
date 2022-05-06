#include <math.h>

#define PI (3.141592653589793)

double generic_function(double x){
    // return PI * x - exp(x);
    return exp(5*x) - 2;
}

double populational_growth(double l){
        double p0 = 1311701;
        double v = 160954 ;
        double p = 2475159;
        return p0 * exp(l) + (v/l)*(exp(l) - 1) - p;
}

double d_populational_growth(double l){
    double p0 = 1311701;
    double v = 160954;
    double p = 2475159;

    return p0 * exp(l) + (v * (exp(l)* l - exp(l) + 1)/ (l * l));
}

double sky_diver_velocity(double m) {
    double g = 9.81;
    double c = 26.61;
    double v = 30.01;
    double t = 7.69;

    return ((g * m) / c) * (1 - exp(-(c/m) * t)) - v;
}

double d_sky_diver_velocity(double m) {
    double g = 9.81;
    double c = 26.61;
    double v = 30.01;
    double t = 7.69;

// e^(-204.631/m) (-75.4389/m - 0.368658) + 0.368658

    return (exp(-204.631 / m))*(-(75.4389/m) - 0.368658) + 0.368658;
}