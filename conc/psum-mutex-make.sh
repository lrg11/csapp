# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o psum-mutex psum-mutex.c csapp.c -lpthread
