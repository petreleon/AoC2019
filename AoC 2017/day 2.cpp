#include <iostream>
#include <string>
#include "clip/clip.h"
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <climits>

using namespace std;
int main() {

    ifstream myfile ("input");
    int result = 0;
    string line;
    int w = 0;
    int k;
    while (std::getline(myfile, line))
    {
        stringstream s(line);
        vector<int> v;
        while (s >> w){
            v.push_back(w);
        }
        for(int i = 0; i < v.size(); i++){
            for(int j = i+1; j < v.size(); j++){
                if(v[i]>v[j]){
                    if(v[i]%v[j]==0){
                        result += v[i]/v[j];
                    }
                }
                else {
                    if(v[j]%v[i]==0){
                        result += v[j]/v[i];
                    }
                }
            }
        }
    }
    cout<<result;
    clip::set_text(to_string(result));
    return 0;
}