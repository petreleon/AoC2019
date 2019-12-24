#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

vector<vector<vector<char>>> transforms(400, {{'.','.','.','.','.'},{'.','.','.','.','.'},{'.','.','.','.','.'},{'.','.','.','.','.'},{'.','.','.','.','.'}});
/*
 *  #####
    .....
    ....#
    #####
    .###.
{{'.','.','.','.','#'},{'#','.','.','#','.'},{'#','.','.','#','#'},{'.','.','#','.','.'}, {'#','.','.','.','.'}}
{{'#','#','#','#','#'},{'.','.','.','.','.'},{'.','.','.','.','#'},{'#','#','#','#','#'},{'.','#','#','#','.'}}

 * */

int bug(char a){
    if(a=='#')
        return 1;
    return 0;
}

int main() {/*
    while(find(transforms.begin(), transforms.end(),(transforms[transforms.size()-1]))==transforms.end()-1){
        vector<vector<char>> &last = transforms[transforms.size()-1];

        vector<vector<char>> temp(5, vector<char>(5));

        for(int i = 0; i<5; i++){
            for(int j = 0; j<5; j++){
                int bugs = 0;
                if(i!=0){
                    if(last[i-1][j]=='#'){
                        bugs++;
                    }
                }
                if(j!=0){
                    if(last[i][j-1]=='#'){
                        bugs++;
                    }
                }
                if(i!=4){
                    if(last[i+1][j]=='#'){
                        bugs++;
                    }
                }
                if(j!=4){
                    if(last[i][j+1]=='#'){
                        bugs++;
                    }
                }
                if(last[i][j]=='#'){
                    if(bugs==1){
                        temp[i][j]='#';
                    }
                    else{
                        temp[i][j]='.';
                    }
                }
                if(last[i][j]=='.'){
                    if(bugs==1 || bugs==2){
                        temp[i][j]='#';
                    }
                    else{
                        temp[i][j]='.';
                    }
                }
            }
        }
        transforms.push_back(temp);
    }
    vector<vector<char>> &repeated = transforms[transforms.size()-1];
    int result = 0;
    for(int i = 0;i<5;i++){
        for(int j = 0;j<5;j++){
            if(repeated[i][j]=='#'){
                result += pow(2, i*5+j);
            }
        }
    }

    cout<<result<<endl;*/
    transforms[200]={{'#','#','#','#','#'},{'.','.','.','.','.'},{'.','.','.','.','#'},{'#','#','#','#','#'},{'.','#','#','#','.'}};
    for(int i = 0; i < 200;i++){
        vector<vector<vector<char>>> temp(400, {{'.','.','.','.','.'},{'.','.','.','.','.'},{'.','.','.','.','.'},{'.','.','.','.','.'},{'.','.','.','.','.'}});
        for(int j = 1; j<399; j++){
            for(int k = 0; k < 5; k++){
                for(int l = 0; l < 5; l++){
                    int bugs = 0;
                    if(l != 2 or k != 2){
                        if(l==0){
                            bugs += bug(transforms[j-1][2][1]);
                        } else if(l-1 == 2 and k == 2){
                            for(int m=0; m<5; m++){
                                bugs += bug(transforms[j+1][m][4]);
                            }
                        } else {
                            bugs += bug(transforms[j][k][l-1]);
                        }

                        if(l==4){
                            bugs += bug(transforms[j-1][2][3]);
                        } else if(l+1 == 2 and k == 2){
                            for(int m=0; m<5; m++){
                                bugs += bug(transforms[j+1][m][0]);
                            }
                        } else {
                            bugs += bug(transforms[j][k][l+1]);
                        }

                        if(k==0){
                            bugs += bug(transforms[j-1][1][2]);
                        } else if(k-1 == 2 and l == 2){
                            for(int m=0; m<5; m++){
                                bugs += bug(transforms[j+1][4][m]);
                            }
                        } else {
                            bugs += bug(transforms[j][k-1][l]);
                        }

                        if(k==4){
                            bugs += bug(transforms[j-1][3][2]);
                        } else if(k+1 == 2 and l == 2){
                            for(int m=0; m<5; m++){
                                bugs += bug(transforms[j+1][0][m]);
                            }
                        } else {
                            bugs += bug(transforms[j][k+1][l]);
                        }
                        if(transforms[j][k][l]=='#'){
                            if(bugs==1){
                                temp[j][k][l]='#';
                            }
                            else{
                                temp[j][k][l]='.';
                            }
                        }
                        if(transforms[j][k][l]=='.'){
                            if(bugs==1 || bugs==2){
                                temp[j][k][l]='#';
                            }
                            else{
                                temp[j][k][l]='.';
                            }
                        }
                    }
                }
            }
        }
        transforms = temp;
    }

    int bugs = 0;
    for(auto &x: transforms){
        for(auto &y:x){
            for(auto&z:y){
                if(z=='#'){
                    bugs++;
                }
            }
        }
    }

    cout<<bugs<<endl;
    if(bugs >= 4053){
        cout<<"your answer is too high"<<endl;
    }
    return 0;
}
