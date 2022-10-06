class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = []
        for i in range(len(s)):
            if s[i] == '(':
                x.append(i)
            elif s[i] == ')':
                y = s[x[-1]: i+1]
                s = s[:x[-1]] + y[::-1] + s[i+1:]
                x.pop()
                
        rev = ""
        for i in range(len(s)):
            if s[i] != ')' and s[i] != '(':
                rev += s[i]
            
        return rev
