# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o psum-local psum-local.c csapp.c -lpthread
