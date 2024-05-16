class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # Thoda Gyaan
        # vacuous statements are true
        # anything(any random string) has nothing("") between any two elements
        # "" is prefix of all strings
        # "" is suffix of all strings
        # "" is present between the "a" and "t" of "rat" beacuse "ra" + "" + "t" = "rat"

        # Functions make code elegant and modular, Python supports nested functions (write function in function)
        def prefix(s1,s2):
            m,n = len(s1),len(s2)
            # "racecar","rating" --> ra
            # "abhishek","abhi" --> abhi
            #pr is common prefix of both arrays
            # Initialize with empty string
            pr = "" 
            # min(a,b) and max(a,b) exist in python and they do what their name suggests :)
            # We don't want to go over array bounds so we would only compare characters till one of string ends
            # A different charact is encountered  
            for i in range(min(m,n)):
                if s1[i]==s2[i]:
                    pr = pr+s1[i] #If same character add to prefix else break the loop
                else:
                    break
            return pr

        # Initialize answer with first string and then check prefix of answer and current string
        # Update the answer according to common prefix 
        res = strs[0]
        for i in range(1,len(strs)):
            # strs[i] and res: prefix
            res = prefix(res,strs[i])
        return res
