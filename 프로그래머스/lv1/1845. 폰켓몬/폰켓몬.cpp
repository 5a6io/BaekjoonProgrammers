#include <vector>
#include <map>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    map <int, int> kind;
   
    for(auto i = nums.begin(); i != nums.end(); i++)
        for(auto j = nums.begin(); j != nums.end(); j++){
            if(kind.size() < nums.size()/2)
                kind.insert({*i, *j});
        }
    
    answer = kind.size();
    
    return answer;
}