#include <string>
#include <vector>

using namespace std;

bool solution(string s) {
    bool answer = true;
    
    if(s.size() < 4 || s.size() > 6 || s.size() == 5)
        return false;
    else{
        for(auto i : s)
            if(isalpha(i)) return false;
        return true;
    }
}