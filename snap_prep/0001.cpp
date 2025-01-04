class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> null;
        map<int, int> num_set;
        for(int i = 0; i < nums.size(); i++){
            int n1 = nums[i];
            int n2 = target - n1;
            auto j = num_set.find(n2);
            if(j != num_set.end()){
                vector<int> ans{i, j->second};
                return ans;
            }
            num_set.insert(pair<int, int>(n1, i));
        }
        return null;
    }
};
