class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int ans = 0;
        for(char stone:stones.toCharArray()){
            if (isJewel(stone, jewels.toCharArray()))
               {ans += 1;}
        }
        return ans;
        
    }
    public boolean isJewel(char c, char[] checkArr){
            for (char jewel : checkArr){
                if (jewel == c)
                   return true;
            } 
            return false; 
        }
}