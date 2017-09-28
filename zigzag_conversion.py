class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        j = 0
        flag = 1
        l = len(s)

        row_list = [[] for x in range(numRows)]
        if numRows == 1 or numRows == l:
            return s

        # O(n) : run for each character in string
        # Once the numRows is reached revert to appending backwards
        for i in range(l):
            if flag == 1:
                row_list[j].append(s[i])
                j = j+1
                j = j % numRows

                if j == 0:
                    j = numRows - 2
                    flag = 0

            elif flag == 0:
                row_list[j].append(s[i])
                j = j-1
                if j < 0:
                    j = 1
                    flag = 1
        res = ''
        for i in row_list:
            for j in i:
                res = res + str(j)

        return res
                    
