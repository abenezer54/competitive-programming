class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        #Using dictionary
        count = 0
        dic = {"type":0, "color":1, "name":2}
        for item in items:
            if item[dic[ruleKey]] == ruleValue:
                count += 1
        return count
        # count = 0
        # if ruleKey == "type":
        #     for i in range(len(items)):
        #         if items[i][0] == ruleValue:
        #             count += 1
        # if ruleKey == "color":
        #     for i in range(len(items)):
        #         if items[i][1] == ruleValue:
        #             count += 1
        # if ruleKey == "name":
        #     for i in range(len(items)):
        #         if items[i][2] == ruleValue:
        #             count += 1
        # return count
