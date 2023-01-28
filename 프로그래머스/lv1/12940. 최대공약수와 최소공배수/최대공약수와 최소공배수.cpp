#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int m) {
    vector<int> answer(2, 1);
    int temp;
    
    if(n > m){
        temp = n;
        n = m;
        m = temp;
    }
    
    int a = n, b = m;
    temp = 0;
    
    while(b%a != 0){
        temp = b%a;
        b = a;
        a = temp;
    }
    
    answer[0] = a;
    answer[1] = (n * m) / answer[0];
    
    return answer;
}