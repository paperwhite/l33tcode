class Solution(object):
    def validPalindrome(self, s):
     
        flag=1
        l = len(s)
        if l==3 and s[0]!=s[2]:
            return False
        if l%2==1:
            ran = l/2+1
        else:
            ran = l/2
        for i in range(ran):

            if s[i]!=s[l-1-i] and flag==1:
                flag=0
                if s[i]==s[l-2-i]:
                    s = s[0:l-1-i] + s[l-i:l]
                elif s[l-1-i]==s[i+1]:
                    s = s[0:i]+s[i+1:l]
                else:
                    return False
                #print s
                l=len(s)
            elif s[i]!=s[l-1-i] and flag==0:
                return False
                
                # Add a check for "ebcbbececabbacecbbcbe"
        return True
