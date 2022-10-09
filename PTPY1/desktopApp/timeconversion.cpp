#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <string.h>
using namespace std;

void  ltrim(string &s) {
    s.erase(s.begin(), find_if(s.begin(), s.end(), [](unsigned char ch) {
        return !::isspace(ch);
    }));
}

void rtrim(string &s) {
    s.erase(find_if(s.rbegin(), s.rend(), [](unsigned char ch) {
        return !::isspace(ch);
    }).base(), s.end());
}

void trim(string &s) {
    ltrim(s); rtrim(s);
}

vector<string> tokenized(string s, char delimeter) {
    vector<string> res;
    int i = s.length() - 1; 
    while (i > 0) {
        if (s[i] == delimeter) {
            int size = s.length() - i + 1;
            res.push_back(s.substr(i+1, size));
            break;
        }
        i--;
    }
    res.push_back(s.substr(0,1));
    res.push_back(s.substr(2,1));
    return res;
}

void printArray(vector<string> arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

string Split(string s) {
    int n = s.length(); string res = "";
    string::iterator it = s.begin();
    while (it != s.end()) {
        if (isupper(*it)) {
            transform(it, it+1, it, ::tolower);
            if (it != s.begin()) res += " ";
        }
        res += *it;
        it++;
    }
    return res;
}

string Combine(string s, string type) {
    string res = ""; string::iterator it = s.begin();
    if (type.compare("C") == 0) {
        res += toupper(*it);
    } else res += *it;
    it++;
    while (it != s.end()) {
        if (*it == ' ') {
            res += toupper(*(it+1));
            it++;
        } else res += *it;
        it++;
    }
    if (type.compare("M") == 0) res += "()";
    return res;
}

string camelCase(string s) {
    vector<string> tokens = tokenized(s, ';');
    if (tokens[1].compare("S")==0) {
        if (tokens[2].compare("M") == 0) return Split(tokens[0].substr(0, tokens[0].length()-2));
        else return Split(tokens[0]);
    } 
    return Combine(tokens[0], tokens[2]);
}

int main() {
    ifstream fin;
    fin.open("input.txt");
    for (string s; getline(fin,s);) {
        string temp = camelCase(s);
        trim(temp);
        cout << temp << endl;
    }
    //read from stdin 
    return 0;
}