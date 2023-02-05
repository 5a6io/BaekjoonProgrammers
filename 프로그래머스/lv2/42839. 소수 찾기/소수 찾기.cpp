#include <string>
#include <map>
#include <algorithm>

using namespace std;

bool isPrime(int n){
    if(n == 0 || n == 1)
        return false;
    for(int i = 2; i*i <= n; i++){
        if(n % i == 0)
            return false;
    }
    return true;
}

int solution(string numbers) {
    int answer = 0;
    map<int, int> prime;
    
    sort(numbers.begin(), numbers.end());
    
    do {
        for(int i = 1; i <= numbers.size(); i++)
            if(isPrime(stoi(numbers.substr(0, i))))
                prime.insert({stoi(numbers.substr(0, i)), 1});
    } while(next_permutation(numbers.begin(), numbers.end()));
    
    return answer = prime.size();
}