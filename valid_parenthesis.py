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
        
        # O(n) solution, iterating over each character of the string
        
        for i in s:
            # if the bracket is an opening bracket, push it onto the stack
            if i =='(' or i =='{' or i =='[':
                st.append(i)
            # if it is a closing bracket, check if the stack is non empty and pop
            elif len(st)!=0:
                x = st.pop()
                # check if the popped element is a valid match for the i-th character, 
                # if not return False because there is a parenthesis mismatch
                if x=='(':
                    if i!= ')':
                        return False
                elif x == '[':
                    if i != ']':
                        return False
                elif x == '{':
                    if i != '}':
                        return False
            # if stack is empty, return False, because there's an extra closing bracket
            else:
                return False
        # if stack is non-empty after all characters have been read, return False, because there are extra opening brackets        
        if len(st)>0:
            return False
        
        return True
