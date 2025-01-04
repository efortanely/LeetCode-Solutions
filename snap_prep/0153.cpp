class Solution {
public:
    int findMin(vector<int>& nums) {
        if(nums.size() == 1){
            return nums[0];
        }
        
        int k = nums.size() / 2;
        vector<int> left = vector(begin(nums), begin(nums) + k);
        vector<int> right = vector(begin(nums) + k, begin(nums) + nums.size());
        
        if(left.size() == 0 || left[left.size()-1] > right[right.size()-1]){
            return findMin(right);
        }else{
            return findMin(left);
        }
    }
};
