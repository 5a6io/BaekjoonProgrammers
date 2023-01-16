using namespace std;

long long solution(int price, int money, int count)
{
    long long answer = -1;
    long long use = 0;
    
    for(auto i = 1; i <= count; i++)
        use += price * i;
    
    if(use - money > 0)
        answer = use - money;
    else
        answer = 0;
    
    return answer;
}