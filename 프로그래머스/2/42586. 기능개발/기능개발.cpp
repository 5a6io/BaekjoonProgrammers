#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> day;
    int release = 1;
    
    for(auto i = 0; i < progresses.size(); i++){
        int r = 100 - progresses[i];
        int s = speeds[i];
        int d = r / s; // 작업 일수
        if(r%s != 0) // 나누어 떨어지지 않으면 하루 더 걸림.
            day.push_back(d+1);
        else
            day.push_back(d);
    }
    
    int prev = day[0];
    for(auto i = 1; i < day.size(); i++){
        if(day[i] <= prev)
            release++;
        else{
            answer.push_back(release);
            release = 1;
            prev = day[i];
        }
        
        if(i == day.size()-1)
            answer.push_back(release);
    }
    
    return answer;
}