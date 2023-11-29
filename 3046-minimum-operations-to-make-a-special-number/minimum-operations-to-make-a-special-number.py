class Solution:
    def minimumOperations(self, num: str) -> int:
        a1 = []
        a2 = []
        found1 = False
        for i in range(len(num) -1, -1,-1):
            if (found1 and num[i] == "0") or (found1 and num[i] == "5"):
                a1.append(i)
                break
            if not found1 and num[i] == "0":
                a1.append(i)
                found1 = True
        found2 = False
        for i in range(len(num) -1, -1,-1):
            if (found2 and num[i] == "2") or found2 and num[i] == "7":
                a2.append(i)
                break
            if not found2 and num[i] == "5":
                a2.append(i)
                found2 = True

        if not a1 and not a2:
            return len(num)
        cur1 = float("inf")
        cur2 = float("inf")
        # print(a1, a2)
        c = False
        if len(a1) > 1:
            cur1 = len(num) - 1 - a1[0] + (a1[0] -a1[1] - 1) 
            c = True
        if len(a2) > 1:          
            cur2 = len(num) - 1 - a2[0] + (a2[0] -a2[1] - 1)   
            c = True
        minn  = min(cur1, cur2)
        if c:   
            return minn
        else:
            return len(num) - num.count("0")
