#include<stdio.h>
#include<math.h>
/* creating a function so that in the future a function with different arguments but same signature can be used */
double function(double x){
	return pow(x,10)-1;
}

/* the method takes a standard in_out function which has both input as well as output to be double*/
double bisection(double (*p)(double),double lower,double upper){
	
	for(int i=0;i<10;i++){
		double mid = (upper+lower)/2.0;
		printf("f(x) - %f   x - %f\n",p(mid),mid);
		if((p(mid)*p(lower))<0){
			upper =mid;
		}
		else{
			lower = mid;
		}

	}
}
double regula_falsi(double (*p)(double),double lower,double upper){
	
}

int main(int argc, char const *argv[])
{
	double t = bisection(function,0,1.3);
	printf("%f\n", t);
	return 0;
}

