class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        lookup = {}
        for domain in cpdomains:
            value, key = domain.split()
            value = int(value)
            i = len(key) - 1
            key = "."  + key
            while i >= 0:
                if  key[i] == ".":
                    if key[i + 1:] not in lookup:
                        lookup[key[i + 1:]] = value
                    else:
                        lookup[key[i + 1:]] += value      
                i -= 1

        ans = []
        for key, value in lookup.items():
            ans.append(str(value) + " " + key)

        return ans