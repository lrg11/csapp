# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o sigint sigint.c csapp.c -lpthread
