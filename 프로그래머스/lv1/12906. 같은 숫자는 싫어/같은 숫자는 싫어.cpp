#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    int i = 0;

    vector<int>::iterator it = arr.begin();
    
    answer.push_back(*it);
    i++;
    for(it = arr.begin()+1; it != arr.end();it++){
        if(*it != arr[i-1]){
            answer.push_back(*it);
        }
        i++;
    }

    return answer;
}