# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o mm mm.c memlib.c csapp.c -lpthread
