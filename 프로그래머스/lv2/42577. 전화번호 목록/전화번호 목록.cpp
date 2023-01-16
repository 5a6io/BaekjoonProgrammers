#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool solution(vector<string> phone_book) {
    sort(phone_book.begin(), phone_book.end());
    for (int i = 0; i < phone_book.size() - 1; i++)
        if (std::equal(phone_book[i].begin(), phone_book[i].end(),phone_book[i + 1].begin(),phone_book[i + 1].begin()+phone_book[i].size()) == true)
            return false;
    return true;
}