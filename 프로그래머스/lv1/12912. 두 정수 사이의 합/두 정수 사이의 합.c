#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long long answer = 0;
    if(b > a)
        for(int i = a; i<=b; i++)
            answer += i;
    else if(b < a)
        for(int i = b; i <= a; i++)
            answer += i;
    else
        return a;
    return answer;
}