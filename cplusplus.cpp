#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

int main() {
    const int MOD = 1000000007;
    int n, k, op, x;
    cin >> n >> k;
    vector<ll> a(n);
    vector<ll> diff(n); // 差分数组
    ll p = n, val; // 记录被变成 0 的位置，及其对应的值
    for(int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end(), greater<ll>());
    val = a[n - 1];
    diff[0] = a[0];
    for (int i = 1; i < n; ++i) diff[i] = a[i] - a[i - 1];
    for (int i = 0; i < k; ++i) {
        cin >> op >> x;
        // op 1
        if (op == 1) {
            diff[0] += x;
            val += x;
        }
        // op 2
        else if (op == 2) {
            diff[0] -= x;
            val -= x;
            while (p > 0 && val < 0) {
                val -= diff[--p];
                //if (val > 0) val = 0;
            }
            if (p == 0 && val < 0) diff[0] = 0, val = 0;
        }
    }
    ll ans = diff[0], cnt = diff[0];
    if (p == 0) ans = (val % MOD)* n;
    else {
        for (int i = 1; i < p; ++i) {
            cnt += diff[i];
            ans += cnt;
            ans %= MOD;
        }
        //ans += (n - p) * val;
    }
    ans %= MOD;
    printf("%lld", ans);
    return 0;
}

/*
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

    /**
	31-2
	31
	Length of string: 5
	String contents: Hello
	**/
/*
	char string[10];
    char* str1 = "01234567891";
   // strcpy( string, str1 );
 	strncpy(string, str1, sizeof(string) - 1); // 使用安全的 strncpy 函数
    string[sizeof(string) - 1] = '\0'; // 手动添加null终止字符
    cout << "str1 contents: " << string << endl;


	return 0;

}
*/




