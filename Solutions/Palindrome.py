class Solution:
    def isPalindrome(self, x: int) -> bool:
        # we converted the number x to string for easy access of digits
        x = str(x)
        # This is 2 pointer approach
        i,j =0,len(x)-1 # i is start and j is at end
        # These two pointers traverse in opposite direction till they meet in middle
        # We check at each iteration that both x[i],x[j] corresponds to same values and then then move i,j
        while i<j:
            if x[i]!=x[j]:
                return False
            i+=1
            j-=1
        return True