/**
problem desccription : https://leetcode.com/contest/weekly-contest-91/problems/lemonade-change/
*/

class Solution {
public: 
        int no_5,no_10,no_20;    
    
public:
    
    bool makeChange(int money){
        
        while(money!=0){
            
            if(no_5==0 && no_10==0 && no_20==0)
                return false;
            
            if(money>=20 && no_20>0){
                money=money-20;
                no_20--;
            }
            else if(money>=10 && no_10>0){
                money=money-10;
                no_10--;
            }
            else if(money>=5 && no_5>0){
                money=money-5;
                no_5--;
            }else
                return false;
        }
        
        return true;
    }
    
    bool lemonadeChange(vector<int>& bills) {        
        
        no_5=0,no_10=0,no_20=0;
        bool ret = false;
        
        for(int i=0;i<bills.size();i++){
            
            switch(bills[i]){
                case 5:  no_5++;
                    break;
                    
                case 10: no_10++;
                    
                         ret = makeChange(5);
                         if(!ret)
                             return false;
                    break;
                    
                case 20: no_20++; 
                        
                         ret = makeChange(15);
                         if(!ret)
                             return false;
                    break;
                    
                default: return false;
                    break;
            }
        }
    
        return true;
    }
};