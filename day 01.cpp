#include <iostream>
#include <string>
#include "clip/clip.h"
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>

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
        s >> w;
        while (w){
            w = max(w/3-2,0);
            result += w;
        }


    }
    cout<<result;
    clip::set_text(to_string(result));
    return 0;
}