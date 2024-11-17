class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ls = len(strs)
        if ls == 1:
            return strs[0]
        strs.sort()
        fst = strs[0]
        lst = strs[-1]
        cnt = 0
        for i,l in enumerate(fst):
            if i < len(lst) and l == lst[i]:
                cnt += 1
            else:
                break
        return strs[0][:cnt]
