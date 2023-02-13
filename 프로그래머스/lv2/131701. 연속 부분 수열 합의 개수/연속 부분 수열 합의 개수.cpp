#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>

using namespace std;

int solution(vector<int> elements) {
    set<int> arr(elements.begin(), elements.end());
    
    for(int i = 2; i <= elements.size(); i++){
        for(int j = 0; j < elements.size(); j++){
            int cnt = 0, sum = 0, index;
            while(cnt != i){
                index = (j+cnt)%elements.size();
                sum += elements[index];
                cnt++;
            }
            arr.insert(sum);
        }
    }
    
    return arr.size();
}