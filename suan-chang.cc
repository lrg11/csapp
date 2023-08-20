
/* node  left right 
 x
/ \ 
y  s
\
 z
 */
unordered_map<node * , int> depthCount;

int depth(node * root) {
    if(!root || !root->left && !root->right) return 0;
    if(!depthCount.count(root->left) ) depthCount[root->left] = depth(root->left);
    if(!depthCount.count(root->right) ) depthCount[root->right] = depth(root->right);
    return max(depthCount[root->left], depthCount[root->right]) + 1;
}
int res = 0;

void maxDistanceRecurive(node * root) {
    if(!root) return; 
    if(root->left && root->right) 
    {
        int depthleft = depth(root->left);
        int depthright = depth(root->right);
        
        res = max(res, depthleft + depthright + 2);
        if(depthleft > depthright) {
            maxDistanceRecurive(root->left);
        }
        else if(depthright > depthleft) {
            maxDistanceRecurive(root->right);
        }
        else {
             maxDistanceRecurive(root->left);
            maxDistanceRecurive(root->right);
            //return;
        }

    }
    else if(root->left) {
        res = max(res, depth(root->left) + 1); 
         maxDistanceRecurive(root->left);
    }
    else if(root->right) {
        res = max(res, depth(root->right) + 1);
        maxDistanceRecurive(root->right);
    }
    else { 
        return;
    }
} 
int maxDistance(node * root) {
    if(!root) return 0;
    

    res = 0;
    maxDistanceRecurive(root);
    return res;
    
} 


// better

class Solution {
private:
    int maxSum = 0;

public:
    int maxGain(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        
        // 递归计算左右子节点的最大贡献值
        // 只有在最大贡献值大于 0 时，才会选取对应子节点
        int leftGain = maxGain(node->left);
        int rightGain = maxGain(node->right);

        // 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
        int priceNewpath;
        if(node->left && node->right) 
        priceNewpath = 2 + leftGain + rightGain;

    else if(!node->left && !node->right) {
        return 0;
    }
     else {   priceNewpath = 1 + leftGain + rightGain;
     }

        // 更新答案
        maxSum = max(maxSum, priceNewpath);

        // 返回节点的最大贡献值
        return 1 + max(leftGain, rightGain);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        if(!root) return 0;
        maxGain(root);
        return maxSum;
    }
};



class Solution {
private:
    int maxSum = INT_MIN;

public:
    int maxGain(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        
        // 递归计算左右子节点的最大贡献值
        // 只有在最大贡献值大于 0 时，才会选取对应子节点
        int leftGain = max(maxGain(node->left), 0);
        int rightGain = max(maxGain(node->right), 0);

        // 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
        int priceNewpath = node->val + leftGain + rightGain;

        // 更新答案
        maxSum = max(maxSum, priceNewpath);

        // 返回节点的最大贡献值
        return node->val + max(leftGain, rightGain);
    }

    int maxPathSum(TreeNode* root) {
        maxGain(root);
        return maxSum;
    }
};


class Solution {
    int ans;
    int depth(TreeNode* rt){
        if (rt == NULL) {
            return 0; // 访问到空节点了，返回0
        }
        int L = depth(rt->left); // 左儿子为根的子树的深度
        int R = depth(rt->right); // 右儿子为根的子树的深度
        ans = max(ans, L + R + 1); // 计算d_node即L+R+1 并更新ans
        return max(L, R) + 1; // 返回该节点为根的子树的深度
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        ans = 1;
        depth(root);
        return ans - 1;
    }
};


//
 int leftans, rightans;
    vector<int> crossdepth(TreeNode* rt){
        if (rt == NULL) {
            return {0, 0}; // 访问到空节点了，返回0
        }
        vector<int> L = crossdepth(rt->left); // 左儿子为根的子树的深度
        vector<int> R = crossdepth(rt->right); // 右儿子为根的子树的深度
        leftans = max(leftans,  L[1] + 1); // 计算d_node即L+R+1 并更新ans
        rightans = max(rightans,  R[0] + 1);
        return {L[1] + 1, R[0] + 1}; // 返回该节点为根的子树的深度
    }
public:
    int longestZigZag(TreeNode* root) {
        leftans = 1;
         rightans = 1;
        crossdepth(root);
        return max(leftans,rightans) - 1;
    }

//
class Solution {
    tuple<int, int, int, int> dfs(TreeNode *root) {
        if (root == nullptr) return {0, 0, 0, 0};
        auto [la, lb, lc, ld] = dfs(root->left);
        auto [ra, rb, rc, rd] = dfs(root->right);
        int v = root->val;
        int x = min({la + ra + (v ? 1 : 0), lb + rb + (v ? 1 : 2), lc + rc + (v ? 1 : 2), ld + rd + (v ? 3 : 2)});
        int y = min({la + ra + (v ? 0 : 1), lb + rb + (v ? 2 : 1), lc + rc + (v ? 2 : 1), ld + rd + (v ? 2 : 3)});
        int z = min({la + ra + (v ? 2 : 1), lb + rb + (v ? 2 : 3), lc + rc + (v ? 0 : 1), ld + rd + (v ? 2 : 1)});
        int k = min({la + ra + (v ? 1 : 2), lb + rb + (v ? 3 : 2), lc + rc + (v ? 1 : 0), ld + rd + (v ? 1 : 2)});
        return {x, y, z, k};
    }

public:
    int closeLampInTree(TreeNode *root) {
        auto [x, y, z, k] = dfs(root);
        return min({x, y + 1, z + 1, k + 2});
    }
};


