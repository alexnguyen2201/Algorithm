//  _                                
// | |                               
// | |__  _ __ ___   ___ _ __  _ __  
// | '_ \| '_ ` _ \ / _ \ '_ \| '_ \ 
// | | | | | | | | |  __/ | | | | | |
// |_| |_|_| |_| |_|\___|_| |_|_| |_|

#include <iostream>

using namespace std;

// complexity: Q(1)
int swap(int arr[],int x,int y){
	int temp = arr[x];
	arr[x]=arr[y];
	arr[y]=temp;
}

//apply lomuto partitioning
//A subarray a[start....end] composed of three segments
//1. a segment with element known to be smaller than pivot(p)
//2. a segment with element known to be greater than pivot(p)
//3. a segment with element yet to be compared to pivot(p)
//Complexity: Q(N)
int lomutoPartition(int arr[],size_t start,size_t end){

	int p = arr[start]; // pivot -> first element
	int s = start;

	for(int i=s+1;i<end;++i){
		if(p>arr[i]){
			++s;
			swap(arr,i,s);
		}
	}
	swap(arr,start,s);
	return s;
}

// quick select algorithm
// first find location of first element with lomuto
// if its not the k.h element, call recursive quickSelect according to s
//Complexity: Best:Q(N)  - Worst:Q(N^2)
int quickSelect(int arr[],int start,int end,int k){

	int s = lomutoPartition(arr,start,end);
	if(s==k-1)
		return arr[s];
	else if(s>start+k-1) return quickSelect(arr,start,s-1,k);
	else return quickSelect(arr,s+1,k-1-s,k);
}

int main(){
	int size=5;
	int arr[size]={5,1,4,2,4};
	//lomutoPartition(arr,0,5);

	for(int i=0;i<size;++i){
		cout<<arr[i]<<" ";
	}cout<<endl;

	cout<<"QuickSelect:  2th:"<<quickSelect(arr,0,size,2)<<endl;

	for(int i=0;i<size;++i){
		cout<<arr[i]<<" ";
	}cout<<endl;

}