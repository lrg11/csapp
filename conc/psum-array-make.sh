# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o psum-array psum-array.c csapp.c -lpthread
