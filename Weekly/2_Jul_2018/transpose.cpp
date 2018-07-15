/**
Prob desc: https://leetcode.com/contest/weekly-contest-92/problems/transpose-matrix/
*/

class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
     
        int rSize = A.size();
        int cSize = A[0].size();
        
        if(rSize==1 && cSize==1)
            return A;
        
        vector<vector<int>> B;
        for(int i=0;i<cSize;i++)
        {
            vector<int> temp;
            for(int j=0;j<rSize;j++){
                temp.push_back(A[j][i]);
            }
            
            B.push_back(temp);
        }
        
        return B;
    }
};