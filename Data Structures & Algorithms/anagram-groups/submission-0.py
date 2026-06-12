class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        data = defaultdict(list)
        for i in range(n):
            sorted_str = sorted(strs[i])
            data["".join(sorted_str)].append(strs[i])
        ans = []
        for ch,ch_list in data.items():
            ans.append(ch_list)

        return ans
        