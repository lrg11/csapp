# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o restart restart.c csapp.c -lpthread
