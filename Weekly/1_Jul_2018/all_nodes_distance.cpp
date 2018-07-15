/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    
    vector<int> mNodeList = null;
    vector<int> mPath2Node = null;
    int depth = 0;
    
    void travelFromNode(TreeNode *root,int K){
        
        if(root==null || k==0)
            return;
        
        mNodeList.push_back(root->val);
        
        travelFromNode(root->left,k-1);
        travelFromNode(root->right,k-1);
    }
    
    TreeNode* checkNode(TreeNode *root,int val){
        
        if(root==null)
            return null;
        
        mPath2Node.push_back(root->val);

        if(root->val == val)
            return root;
        
        depth = depth + 1;
        
        TreeNode* result = checkNode(root->left,val);

        if(result)
        	return result;
        else
        {
        	mPath2Node.pop_back();
        	return checkNode(root->right,val);
        }
        
    }
    
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        
        mNodeList = new vector<int>();
        
        if(root==null)
            return null;
        
        vector<int> mVector = new vector<int>();
        if(root->val==val)
        {
            mNodeList = travelFromNode(root->left,K);
            vector<int> mTempVector = travelFromNode(root->right,K);
            mNodeList.insert(mNodeList.end(), mTempVector.begin(), mTempVector.end());
            
            return mNodeList;
        }
        
        TreeNode *node = null;

        int dir = 0;//left
        depth = 0;
        node = checkNode(root->left,target->val);
        if(node==null)
        {
        	dir = 1;
        	depth = 0;
        	node = checkNode(root->right,target->val);
        }

        if(dir==0)// traverse the right tree
        {
        	mNodeList = travelFromNode(root->right,K-depth);
        }
        else
        {
        	mNodeList = travelFromNode(root->left,K-depth);
        }

        mNodeList.insert(mNodeList.end(), mPath2Node.begin(), mPath2Node.end());

        return mNodeList;
    }
};