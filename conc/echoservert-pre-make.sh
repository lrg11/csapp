# gcc -O2 -Wall -I . -c csapp.c -o csapp.o 
gcc  -O2 -Wall -I . -o echoservert_pre echoservert_pre.c echo_cnt.c sbuf.c csapp.c -lpthread
