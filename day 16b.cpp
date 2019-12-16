#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <sstream>

using namespace std;
int main(){
    string str = "59740570066545297251154825435366340213217767560317431249230856126186684853914890740372813900333546650470120212696679073532070321905251098818938842748495771795700430939051767095353191994848143745556802800558539768000823464027739836197374419471170658410058272015907933865039230664448382679990256536462904281204159189130560932257840180904440715926277456416159792346144565015659158009309198333360851441615766440174908079262585930515201551023564548297813812053697661866316093326224437533276374827798775284521047531812721015476676752881281681617831848489744836944748112121951295833143568224473778646284752636203058705797036682752546769318376384677548240590";
    //str = "03081770884921959731165446850517";
    stringstream ss(string(str.begin(), str.begin() + 7));
    int offset;
    ss >> offset;
    long new_size = str.size()*10000-offset;// 650*10000 -  5974057
    long rest = new_size%str.size();
    long div = new_size/str.size();
    string new_str(str.end()-rest, str.end());
    for(int i = 0; i < div; i++){
        new_str+=str;
    }
    new_str += "0";
    for(int i = 0; i < 100; i++){
        //string new_str2 = new_str;
        for(long j = new_str.size()-2; j >= 0; j--){
            new_str[j] = '0' + (new_str[j] - '0' + new_str[j+1] - '0') % 10;
        }
    }
    new_str = string(new_str.begin(), new_str.end() - 1);
    cout<<new_str.length()+offset<<endl;
    string output_str = string(new_str.begin(), new_str.begin()+8);
    cout<<output_str<<endl;
    //bad answer 98147575
    return 0;
}
