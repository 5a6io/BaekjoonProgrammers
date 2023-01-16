#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    int max = *max_element(priorities.begin(), priorities.end());
    vector<int> work;

    int i = 0;
    while(i <= priorities.size()){
        if(max == 0)
            break;
        if(priorities[i] == max) {
            work.push_back(i + 'A');
            priorities[i] = 0;
            max = *max_element(priorities.begin(), priorities.end());
            i++;
        }
        else if(max != 0 && i == priorities.size())
            i = 0;
        else
            i++;
    }

    int j = 1;
    for(auto i:work){
        if(i == location+'A') {
            answer = j;
            break;
        }
        j++;
    }

    return answer;
}