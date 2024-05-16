class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for br in s:
            if br in ["(", "[", "{"]:
                stack.append(br)
            else:
                if not stack:
                    return False
                top_value = stack[-1]
                if ((br == ")" and top_value == "(") 
                    or (br == "}" and top_value == "{")
                    or (br == "]" and top_value == "[")):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return  True