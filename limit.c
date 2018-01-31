#include <stdio.h>
#include <math.h>


double f(double h) {
    return (pow(2.0 + h, 3.0) - pow(2.0, 3.0)) / h;
}


int main(int argc, char **argv) {
    printf("%.10lf\n", f(0.001));
    printf("%.10lf\n", f(0.0001));
    printf("%.10lf\n", f(0.00001));
    printf("%.10lf\n", f(0.000001));
    printf("expect 12.0000...%.10lf\n", f(0.0000001));
    printf("expect 11.99... %.10lf\n", f(0.00000001));
    printf("%.10lf\n", f(0.000000001));
    printf("%.10lf\n", f(0.0000000001));
    printf("%.10lf\n", f(0.00000000001));
    printf("%.10lf\n", f(0.000000000001));
    printf("%.10lf\n", f(0.0000000000001));
    printf("%.10lf\n", f(0.00000000000001));
    printf("%.10lf\n", f(0.000000000000001));
    printf("%.10lf\n", f(0.0000000000000001));
    printf("%.10lf\n", f(0.00000000000000001));
    printf("%.10lf\n", f(0.000000000000000001));
}
