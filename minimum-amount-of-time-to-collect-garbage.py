class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix = [0] * (len(travel) + 1)
        for i in range(len(travel)):
            prefix[i + 1] = prefix[i] + travel[i]

        count = {"G":0, "P": 0, "M":0}
        lastindex = defaultdict(int)
        for s in garbage:
            count["G"] += s.count("G")
            count["M"] += s.count("M")
            count["P"] += s.count("P")

        for i, s in enumerate(garbage):
            if "G" in s:
                lastindex["G"] = i
            if "P" in s:
                lastindex["P"] = i
            if "M" in s:
                lastindex["M"] = i

        ans = 0
        for key, value in lastindex.items():
            ans += (count[key] + prefix[value])

        return ans