/*# include <iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    bool divided=false;
    for(int d=2;d<n;d++){
        if(n%d==0){
            divided==true;
        }
        if (divided){1
            cout<<"not prime"<<endl;
        } else{
            cout<<"prime"<<endl;
        }
    }


for(int i=0;i<5;i++){
cout<<i<<"";
i=i-1;}
    return 0;

for (int i=0;i<2;i=i+1){
    for(int j=0;j<2;j=j+1){
        if(j==1)
        break;
        cout<<j<<"";
    }
}
for(int i=0;i<5;i=i+1){
    if(i==2)
    continue;
    cout<<i<<"";
}


int n,r;
cin>>n>>r;
int fact_n=1;
int i=1;
while(i<=n){
    fact_n=fact_n*i;
    i++;
}
int fact_r=1;
i=1;
while(i<=r){
    fact_r=fact_r*i;
    i++;
}
int fact_n_r=1;
i=1;
while (i <=n - r){
    fact_n_r=fact_n_r*i;
    i++;
}
cout<<fact_n/(fact_r*fact_n_r)<<endl;


# include <iostream>
using namespace std;
int factorial(int n){
    int ans=1;
    int i=1;
    while(i<=n){
        ans = ans*i;
        i++;
    }
    return ans;
}
int main(){
    int n,r;
    cin>>n>>r;
    //int output = factorial(5);
    //cout<<output<<endl;
    int fact_n=factorial(n);
    int fact_r=factorial(r);
    int fact_n_r=factorial(n-r);
    int ans=fact_n/(fact_r*fact_n_r);
    cout<<ans<<endl;
    */
// # include <iostream>
// using namespace std;
/*void print_1_to_n(int n){
for(int i=1;i<=n;i++){
    cout<<i<<endl;
}
}
//bool isprime(int n){
   /* int d=2;
    while(d<n){
        if(n%d==0){
            return false;
        }
        d++;
    }return true;  
}*/
// int main(){
//     int startvalue,endvalue,step,c,f;

//     cout<<"Start value: ";
//     cin>>startvalue;
//     cout<<"end value: ";
//     cin>>endvalue;
//     cout<<"Gap value: ";
//     cin>>step;

//     for(f=startvalue;f<=endvalue;f= f+ step){
// c=(f-32)*5/9;
// cout<<f<<" ";
// cout<<c<<endl;
//     }
//}
   /* float fahren,celcius;
    cout<<"enter";
cin>>fahren;
celcius=(9/5)*fahren+32;
cout<<celcius<<endl;
    }*/

    /*bool ans=isprime(31);
    cout<<ans<<endl;
    ans=isprime(85);
    cout<<ans<<endl;

 */
//  #include<iostream>
//  #include<climits>
//  using namespace std;
//  int main(){
//     int n;
//     cin>>n;
    
//     int input[100];
//     for(int i=0;i<n;i++){
//         cin>>input[i];
//     }
//     for(int i=0;i<n;i++){
//         cout<<input[i]<<endl;
//     }
//     int max= INT_MIN;
//     for(int i=0;i<n;i++){
//         if(input[i]>max){
//             max=input[i];
//         }
//     }
//     cout<<"max : "<<max<<endl;

//  }

// #include<iostream>
// using namespace std;
// int main(){
// int n;
// cin>>n;
// int input[3],sum=0,i;

// for(int i=0;i<n;i++){
//     cin>>input[i];
// }
// //cout<<n<<" ";
//  for(int i=0;i<n;i++){
//      sum=sum+input[i];
// }
//      cout<<sum<<endl;


// }
// # include <iostream>
// using namespace std;
// int main(){
// int arr[10],n,i,k,t;
// cout<<"enter no. of times loop run: ";
// cin>>k;
// for(int a=1;a<=k;a++){
// cout<<"enter the length of array";
// cin>>t;
// cout<<"enter numbers";
// for(i=0;i<t;i++)
// cin>>arr[i];
// cout<<"\nenter number to search ";
// cin>>n;
// for(i=0;i<10;i++)
// {
//     if(arr[i]==n)
//     { 
//         cout<<"\nfound at "<<i;
//         break;
        
// }
// }

// if(arr[i]!=n)
// {
//     cout<<"not found";
// }
    
       
// cout<<endl;
// }
// return 0;    
// }

// #include<iostream>
// using namespace std;
// int main(){
// int arr[10],a,k,f,n;
// cout<<"no. of times loop will run: ";
// cin>>k;
// cin>>n;
// int t=2*n-1;
// int p=((n+1)/2);
// for(int a=1;a<=k;a++){
//     // cout<<"enter the length of array";
//     // cin>>n;
//     cout<<"enter numbers";
//     for(f=1;f<=p;n++)
//     cin>>arr[p];
// }
// #include<iostream>
// using namespace std;
// int main(){
// int n;
// int start=0,end=n-1;
// int val=1;

// 
// #include<iostream>
// using namespace std;
// int main(){
//     int arr[10],n,k=1;
//     cin>>n;
//     for( int i=0;i<(n+1)/2;i++,k++){
//     cout<<(arr[i]=2*k-1);

// }
// //  cout<<k;

//     k=n/2;
// for(int i=(n+1)/2;i<n;i++,k++){
//     cout<<(arr[i]=(n+k)*2);  
// }
// }
// #include <iostream>
// using namespace std;
// int main(){

//     int val=1;
//     arr=[]
//     int start = 0 ,end = n-1;
//     while(start<=end){
//         if(val%2==1){
//     arr[start]=val;
//     val++;
//     start++;
//   }  
//         else{
//             arr[end]=val;
//     val++;
//     end--;
//         }
//     }
// }

// int main()
// {
// 	int t;
// 	cin >> t;
// 	while (t--)
// 	{
// 		int n;
// 		cin >> n;

// 		int *arr = new int[n];
// 		arrange(arr, n);
// 		for (int i = 0; i < n; i++)
// 		{
// 			cout << arr[i] << " ";
// 		}
// 		cout << endl;
// 		delete [] arr;
// 	}	
// }