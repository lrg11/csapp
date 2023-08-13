# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o echoservers echoservers.c echo.c csapp.c -lpthread
