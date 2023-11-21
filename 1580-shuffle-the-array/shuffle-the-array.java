class Solution {
    public int[] shuffle(int[] nums, int n) {
        ArrayList<Integer> ans = new ArrayList<>();

        for(int i = 0; i < n;i++){
            ans.add(nums[i]); ans.add(nums[i+n]);
        }
        
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++){
            res[i] = ans.get(i);
        }

        return res;
    }
}