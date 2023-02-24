#include <string>
#include <vector>

using namespace std;

int solution(int a, int b, int n) {
    int answer = 0;
    int new_coke = 0;
    int rest_coke = 0;
    
    while (n >= a) {
        if(n % a != 0){
            new_coke = n / a * b;
            rest_coke = n % a;
            answer += new_coke;
            n = new_coke + rest_coke;
        }
        else {
            new_coke = n / a * b;
            answer += new_coke;
            n = new_coke;
        }
    }
    
    return answer;
}