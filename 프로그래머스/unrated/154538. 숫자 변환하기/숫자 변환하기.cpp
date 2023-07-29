#include <string>
#include <vector>

using namespace std;

int solution(int x, int y, int n) {
    vector<int> result(y + 1, INT32_MAX-1);
    
    result[x] = 0;
    for(int i = x + 1; i <= y; i++){
        if(i - n >= x) result[i] = min(result[i], result[i - n] + 1);
        if(i % 2 == 0 && i / 2 >= x) result[i] = min(result[i], result[i / 2] + 1);
        if(i % 3 == 0 && i / 3 >= x) result[i] = min(result[i], result[i / 3] + 1);
    }
    
    return result[y] != INT32_MAX - 1 ? result[y] : -1;
}