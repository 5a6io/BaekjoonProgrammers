#include <stack>
#include <string>
using namespace std;

int solution(string s)
{
    stack<char> c;
    if(s.size() == 1)
            return 0;
    
    for(int i = 0; i < s.size(); i++){
        if(!c.empty() && c.top() == s[i])
            c.pop();
        else
            c.push(s[i]);
    }
    
    if(!c.empty())
        return 0;
    else
        return 1;
}