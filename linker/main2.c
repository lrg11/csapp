#include <stdio.h>
#include "vector.h"


int x[2] = {1, 2};
int y[2] = {3, 4};


int main() {
	int z[2];
	addvec(x, y, z, 2);
	printf("z = [%d, %d] \n", z[0],z[1]);
	return 0;
}

/*
 gcc -static -o prog2c -L . -lvector main2.c
/usr/bin/ld: /tmp/cchnAXeK.o: in function `main':
main2.c:(.text+0x36): undefined reference to `addvec'
collect2: error: ld returned 1 exit status

need first obj, then archive 
gcc -static -o prog2c main2.c ./libvector.a
*/