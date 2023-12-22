class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> umap;
        int n = nums.size();
        
        for(int i = 0; i < n; i++){
            int c = target - nums[i];
            if( umap.find(c) != umap.end()){
                cout << c;
                return {umap[c], i};
            }
            umap[nums[i]] = i;                
        }

        return {};
    }
};