class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> nums2;
        for(int i = 0; i < nums.size(); i++){
            if(nums2.find(nums[i]) != nums2.end()){
                return true;
            }
            nums2.insert(nums[i]);
        }
        return false;
    }
};
