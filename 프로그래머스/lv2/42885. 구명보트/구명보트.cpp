#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    vector<int> boat;

    sort(people.begin(), people.end());
    auto p1 = people.begin();
    auto p2 = people.end() - 1;
    
    while(p1 <= p2){
        if(*p1 + *p2 > limit){
            boat.push_back(*p2);
            p2--;
        }
        else if(*p1 + *p2 <= limit){
            boat.push_back(*p1 + *p2);
            p1++;
            p2--;
        }
        else if(p1 == p2)
            boat.push_back(*p1);
    }
    return answer = boat.size();
}