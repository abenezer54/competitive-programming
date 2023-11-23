class Solution {
    public int[] runningSum(int[] nums) {
        int[] prefix = Arrays.copyOf(nums, nums.length);
        for(int i = 1; i < nums.length; i++){
            prefix[i] += prefix[i - 1];
        }
        
        return prefix;       
    }
}