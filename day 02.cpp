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
    map<char, int> w;
    ifstream myfile ("input");
    int result = 0;
    int pair1= 0 , pair2 = 0;
    string line;
    while (std::getline(myfile, line))
    {
        replace(line.begin(), line.end(), ',',' ');
        stringstream ss(line);
        vector<int> l;
        vector<int> r;
        int temp;
        while (ss>>temp){
            l.push_back(temp);
            r.push_back(temp);
        }


        for(int k=0;k<=99;k++)for(int j=0;j<=99;j++){
            l=r;
            l[1]=j;
            l[2]=k;
            int i = 0;
            while (l[i] != 99) {
                if (l[i] == 1) {
                    l[l[i + 3]] = l[l[i + 1]] + l[l[i + 2]];
                }
                if (l[i] == 2) {
                    l[l[i + 3]] = l[l[i + 1]] * l[l[i + 2]];
                }
                i += 4;
            }
            if(l[0]==19690720){
                result = 100*j+k;
                goto endOfLoop;
            }

        }
    }
    endOfLoop:
    cout<<result;
    clip::set_text(to_string(result));
    return 0;
}