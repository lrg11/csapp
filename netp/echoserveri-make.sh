# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o echoserveri echoserveri.c echo.c csapp.o -lpthread
