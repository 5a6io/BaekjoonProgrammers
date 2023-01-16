#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    string str = to_string(x);
    int sum = 0;
    
    for(auto i = str.begin(); i != str.end(); i++)
        sum += (*i-'0');
    
    if(x%sum != 0)
        answer = false;
    
    return answer;
}