#include <bits/stdc++.h>
using namespace std; 

int main()
{
    string s;
    int n;
    int sX,sY;
    int dX,dY;
    cin>>s;
    cin>>n;
    cin>>sX;
    cin>>sY;
    cin>>dX;
    cin>>dY;
    int t = s.length()/n;
    int k = 0;
    vector<vector<int>> V(t,vector<int>(n,0));
   int i,j;
   i=0;
   while(i<t){
        j=0;
        while(j<n){
            switch(s[k])
            {
                case '1' :
                    V[i][j]=1;
                    break;
                default : 
                    V[i][j] = 0;
            }
            k++;
            j++;
        }  
       i++;
    }
    
     if(V[sX][sY] != 0 || V[dX][dY] != 0)  
          return -1;        
       
        queue<pair<int, int>> q;
        q.push({sX,sY});
         int ans = 0;

        vector<int> xt1 = {0,0,1,-1};
        vector<int> yt2 = {1,-1,0,0};
       
        do{
           int size = q.size();
           int xa1, ya2, xs1, ys2; 
            
            while(size--){
                xa1 = q.front().first;
                ya2 = q.front().second;
                q.pop(); 
               
                if(xa1 == dX) 
                    if(ya2 == dY) {
                      cout<< ans; 
                      return 0; 
                  }  
              i=0; 
              while(i<4){
                    xs1 = xa1 + xt1[i];
                    ys2 = ya2 + yt2[i];
                                    }
                         i++;
                  }
            }
             ans++;   
        }while(!q.empty());
    
    return 0;
}

