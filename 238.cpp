class Solution{
public:
    vector<int> productExceptSelf(vector<int>& nums){
        vector<int> M1(nums.size(), 1);
        vector<int> M2(nums.size() + 1, 1);
        vector<int> nums2(nums.size(), 0);
        
        for(int i = 0; i < nums.size(); i++){
            int left = i == 0? 1 : M1[i-1];
            M1[i] = left * nums[i];
        }
            
        for(int i = nums.size() - 1; i >= 0; i--){
            int right = i == nums.size() - 1? 1 : M2[i+1]; 
            M2[i] = right * nums[i];
        }

        for(int i = 0; i < nums.size(); i++){
            int left = i == 0? 1 : M1[i-1];
            nums2[i] = left * M2[i+1];
        }
              
        return nums2;
    }
};
