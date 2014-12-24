#include<iostream>
#include<algorithm>
using namespace std;

int max(int i,int j,int k){
	int w = max(i,j);
	w=max(w,k);
	return w;
	
}

int main(){
	
	int j ; 
	
	cin >>j;
	
	
	while(j--){
		int k,w;
		cin>>k>>w;
		int gd[k][w];
		int ans[k][w];
		for(int x = 0;x<k;x++){
			for(int y=0;y<w;y++){
				cin>>gd[x][y];
				if (x==0){
				ans[x][y]=gd[x][y];
				
				}
			}
		}
		
for(int a=1;a<k;a++){
			for(int b=0;b<w;b++){
				if (b==0){
					ans[a][b]=max(ans[a-1][b]+gd[a][b],ans[a-1][b+1]+gd[a][b]);
				}
				else if (b==(w-1)){
					ans[a][b]=max(ans[a-1][b]+gd[a][b],ans[a-1][b-1]+gd[a][b]);
				}
				else{
					ans[a][b]=max(ans[a-1][b]+gd[a][b],ans[a-1][b-1]+gd[a][b],ans[a-1][b+1]+gd[a][b]);
				}
				
				
			}
			
		}
		cout<<*max_element(ans[k-1],ans[k-1]+w)<<endl;
		
	}
	

}
