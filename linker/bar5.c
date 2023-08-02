double x ;

void f() {
	x = -0.0;
	// 负零的双精度浮点数覆盖x和y的两个int型内存位置（4+4 = 8，double）
	// 请使用-fno-common标志，让链接器在遇到多重定义的全局符号时触发一个错误，gcc -fno-common  foo5.c bar5.c -o foobar5
	// 或者使用-Werror选项，把所有警告变为错误
}