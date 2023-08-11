# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o setjmp setjmp.c csapp.c -lpthread
