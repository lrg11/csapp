#include <stdio.h>
int f() {
	static int x = 0;
	return x;

}

//int x = 15213;
//int y = 15212;

int g() {
	static int x = 1;
	return x;

}

int main() {
	// f()
	int x = g();
	printf("x = 0x%x \n", x);
	// x = 0x0 
	return 0;
}

