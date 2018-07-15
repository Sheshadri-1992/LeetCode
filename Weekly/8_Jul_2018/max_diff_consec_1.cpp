/**
prob desc: https://leetcode.com/contest/weekly-contest-93/problems/binary-gap/
*/

class Solution {
public:
    
    string returnBinary(int N) {
        
        string binary="";
        int num = 0;
        char ch;
       
        // cout<<"N is "<<N<<endl;
        while(N!=0){
            
            num = N%2;
            ch = num + '0';
            N = N/2;
            // cout<<"N is "<<N<<" ch is "<<ch<<endl;
            binary = binary + ch;
        }
        
        string result = "";
        int i=binary.length()-1;
        
        while(i>=0){
            result = result + binary[i];
            i--;
        }
        
        return result;
        
    }
    
    int binaryGap(int N) {
        
        string binary = returnBinary(N);
        
        int first = -1;
        int second = -1;
        
        int i=0;
        
        // cout<<" binary digit is "<<binary<<endl;
        
        int result = 0;
        
        while(binary[i]!='\0'){
            
            if(binary[i]=='1'){
                first = second;
                second = i;
                
                result = max(result, second-first);
            }
            
            i++;
        }
        
        if(first==-1)
            return 0;
        
        return result;
    }
};