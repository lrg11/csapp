#include <iostream>
#include <string>
#include <cstring>

using namespace std;
 
int func(string a, string const & b, string const & c){
	a.insert(a.size(), "-");
	a.insert(0, c);
	a.insert(a.size(), b);
	cout << a << endl;
	return atoi(a.c_str());
}


int main()
{
	string a = "1";

	cout << func(a, "2", "3") << endl;


    std::string str = "Hello\0World"; // 包含了null字符
    std::cout << "Length of string: " << str.length() << std::endl; // 输出字符串长度
    std::cout << "String contents: " << str << std::endl; // 输出字符串内容

    /*
	31-2
	31
	Length of string: 5
	String contents: Hello
	*/

	char string[10];
    char* str1 = "01234567891";
   // strcpy( string, str1 );
 	strncpy(string, str1, sizeof(string) - 1); // 使用安全的 strncpy 函数
    string[sizeof(string) - 1] = '\0'; // 手动添加null终止字符
    cout << "str1 contents: " << string << endl;


	return 0;

}


