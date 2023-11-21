class Solution {
    public int[] buildArray(int[] nums) {
        int len = nums.length;
        int[] ans = new int[len];

        for (int i = 0; i < len; i++){
            int idx = nums[i];
            ans[i] = nums[idx];
        }

        return ans;
        
    }
}