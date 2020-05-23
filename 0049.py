class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for i in range(len(strs)):
            sort = ''.join(sorted(strs[i]))
            if sort in dic:
                dic[sort].append(strs[i])
            else:
                dic[sort] = [strs[i]]
        return dic.values()
