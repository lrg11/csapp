# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o echoserverp echo.c echoserverp.c csapp.c -lpthread
