# 11 container with most water
class Solution {
    public int maxArea(int[] height) {
        int n = height.length;
        int left = 0, right = n - 1;
        int ans = 0;
        while (left < right) {
            ans = Math.max(ans, (right - left) * Math.min(height[left], height[right]) );
            if(height[left] < height[right]){
                left += 1;
            }
            else {
                right -= 1;
            }
        }
        return ans;
    }
}


// 3 sum
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> rows = new ArrayList<>();
        for(int i = 0; i < n - 2; i++){
            if (i >= 1 && nums[i] == nums[i - 1]) {
                continue;
            }
            int target = -nums[i], left = i + 1, right = n - 1;
            while (left < right) {
                if(nums[left] + nums[right] == target) {
                    rows.add(new ArrayList<>(List.of(nums[i], nums[left], nums[right])));
                    left ++;
                    while (left <right && nums[left] == nums[left - 1])
                         left++;
                    right--;
                    while (left < right && nums[right + 1] == nums[right])
                         right--;
                }
                else if (nums[left] + nums[right] < target) {
                    left++;
                }
                else {
                    right--;
                }
            }
        }

    
        return rows;
    }
}


// find all anagrams in a string
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int sl = s.length(), pl = p.length();
        if(sl < pl) {
            return new ArrayList<Integer>();
        }
        List<Integer> ans = new ArrayList<Integer>();
        int[] sc = new int[26];
        int[] pc = new int[26];
        for(int i = 0; i < pl; i++) {
            sc[s.charAt(i)-'a']++;
            pc[p.charAt(i)-'a']++;
        }
        if (Arrays.equals(sc, pc)){
            ans.add(0);
        }
        for(int i = 0; i < sl-pl; i++) {
            sc[s.charAt(i) -'a']--;
            sc[s.charAt(i + pl) -'a']++;
            if (Arrays.equals(sc, pc)){
                ans.add(i+1);
             }
        }
        return ans;
    }
}

//binary tree inorder traversal
//54346396842

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> ans = new ArrayList<>();
    public void dfs(TreeNode root){
        if(root == null) return;
        dfs(root.left);
        ans.add(root.val);
        dfs(root.right);
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        dfs(root);
        return ans;
    }
}