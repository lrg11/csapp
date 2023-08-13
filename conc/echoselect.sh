# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o echoselect echoselect.c echo.c csapp.c -lpthread
