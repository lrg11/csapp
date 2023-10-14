#include <iostream>
using namespace std;

int&& value = 520;
class Test
{
public:
    Test()
    {
        cout << "construct: my name is jerry" << endl;
    }
    ~Test()
    {
        cout << "deconstruct: my name is jerry" << endl;
    }
    Test(const Test& a)
    {
        cout << "copy construct: my name is tom" << endl;
    }
};

Test getObj()
{
    return Test();
}

int main()
{
    int a1;
    //int &&a2 = a1;        // error
    //Test& t = getObj();   // error
    Test && t2 = getObj();
    const Test& t1 = getObj();
    return 0;
}


