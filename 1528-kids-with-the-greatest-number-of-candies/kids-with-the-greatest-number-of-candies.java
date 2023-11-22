class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxCandy = 0;
        for (int num : candies) {
            if (maxCandy < num)
                maxCandy = num;
        }

        List<Boolean> ans = new ArrayList<>();

        for (int i = 0; i < candies.length; i++) {
            if (candies[i] + extraCandies >= maxCandy)
                ans.add(true);
            else
                ans.add(false);
        }

        return ans;
    }
}
