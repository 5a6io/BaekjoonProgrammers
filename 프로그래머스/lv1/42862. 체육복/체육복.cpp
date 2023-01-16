#include <vector>
#include <map>

using namespace std;
int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    map<int,int> student;
    
    for(auto i:lost) student[i] -= 1;
    for(auto i:reserve) student[i] += 1;
    
    for(auto i = 1; i <= n; i++){
        if(student[i] == -1){
            if(student[i-1] == 1){
                student[i] = student[i-1] = 0;
            }
            else if(student[i+1] == 1){
                student[i] = student[i+1] = 0;
            }
        }
    }
    
    for(auto i = 1; i <= n; i++)
        if(student[i] != -1)
            answer++;

    return answer;
}