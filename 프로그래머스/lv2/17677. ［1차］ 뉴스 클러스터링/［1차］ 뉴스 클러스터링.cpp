#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <iostream>

using namespace std;

int solution(string str1, string str2) {
    int answer = 0;
    double similar = 0.0;
    vector<string> s1, s2;
    vector<string> uni, inter;
    
    for(int i = 0; i < str1.size(); i++)
        str1[i] = tolower(str1[i]);
    
    for(int i = 0; i < str2.size(); i++)
        str2[i] = tolower(str2[i]);
    
    for(int i = 0; i < str1.size() - 1; i++) 
        if(isalpha(str1[i]) && isalpha(str1[i + 1]))
           s1.push_back(str1.substr(i, 2));
    
    for(int i = 0; i < str2.size() - 1; i++)
        if(isalpha(str2[i]) && isalpha(str2[i + 1]))
           s2.push_back(str2.substr(i, 2));
    
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    
    set_union(s1.begin(), s1.end(), s2.begin(), s2.end(), back_inserter(uni));
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), back_inserter(inter));
    
    if(uni.empty())
        similar = 1 * 65536;
    else
        similar = (double)inter.size() / (double)uni.size() * 65536;
    
    return answer = similar;
}