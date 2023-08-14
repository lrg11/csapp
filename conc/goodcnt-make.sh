# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o goodcnt goodcnt.c csapp.c -lpthread
