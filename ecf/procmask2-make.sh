# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o procmask2 procmask2.c csapp.c -lpthread
