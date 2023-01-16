#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    int equal_x = 0, not_equal_x = 0, count = 0;
    for(auto i = 0; i < s.size(); i++){
        char x = s[i];
        for(auto j = i; j < s.size(); j++){
            count++;
            if(s[j] == x)
                equal_x++;
            else if(s[j] != x)
                not_equal_x++;
            if(equal_x == not_equal_x){
                i = j;
                x = s[i];
                answer++;
                count = equal_x = not_equal_x = 0;
                break;
            }
            else if(count==2 && not_equal_x != 0){
                i = j;
                x = s[i];
                answer++;
                count = equal_x = not_equal_x = 0;
                break;   
            }
            if(j == s.size()-1){
                i = j;
                answer++;
            }
        }
    }
    
    return answer;
}