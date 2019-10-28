class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        if(nums1.size() > nums2.size()){
            return intersect(nums2, nums1);
        }
        
        unordered_map<int, int> dic;
        
        for(int n : nums1){
            ++dic[n];
        }
        
        int i = 0;
        for(int n : nums2){
            if(dic.find(n) != dic.end()){
                nums1[i++] = n;
                dic[n]--;
                if(dic[n] == 0){
                    dic.erase(n);
                }
            }
        }
        
        return vector(begin(nums1), begin(nums1) + i);
    }
};
