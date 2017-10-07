"""
@author: Shibani
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """ 
        st = []
        
        for i in s:
            #print i
            if i =='(' or i =='{' or i =='[':
                st.append(i)
            elif len(st)!=0:
                x = st.pop()
                if x=='(':
                    if i!= ')':
                        return False
                elif x == '[':
                    if i != ']':
                        return False
                elif x == '{':
                    if i != '}':
                        return False
            else:
                return False
                
        if len(st)>0:
            return False
        
        return True
