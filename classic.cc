#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    
    int m = a.size();
    int n = b.size();

    int maxi = -1;

    int maxn = 0;
    int len = 0;
    int i = 0;
    int j = n - 1;
    while (i < m) {
        int row = i;
        int col = j;
        int len = 0;
        while(row < m && col < n){
            if(a[row] == b[col]) {
                len+= 1;
                if (len > maxn) {
                    maxn = len;
                    maxi = row;
                }          
            }
            else 
                len = 0;
            row+= 1;
            col+= 1;
        }
            
        if(j > 0)
            j -= 1;
        else
            i+= 1;
    }
               

    if(maxi == -1)
        cout << -1;
    else
        cout << a.substr(maxi - maxn + 1, maxn);

}
// 64 位输出请用 printf("%lld")