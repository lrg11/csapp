#include "csapp.h"

int main() {
	pid_t pid;
	int x = 2;
	pid = Fork();
	if(pid == 0) {
		printf("child: x = %d\n", ++x);
		//exit(0);
	}
	else printf("parent: x = %d\n", --x);
	printf("parent: x = %d\n", --x);
	exit(0);
}
