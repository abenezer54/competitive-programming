class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] sortedArr = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sortedArr);
        System.out.println(sortedArr);
        int[] ans = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            for (int j = 0; j < nums.length; j++){
                if (sortedArr[j] == nums[i])
                    {
                        ans[i] = j;
                        break;
                    }
            }
        }
        
        return ans;
    }
}