class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxWealth = 0;
        for(int[] account:accounts){
            int currentSum = 0;
            for(int num:account){
                currentSum += num;
            }
            if (currentSum > maxWealth)
                maxWealth = currentSum;
            
        }
        return maxWealth;
    }
}