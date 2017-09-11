class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m==0 :
            flag = 0
        else:
            flag=1
            n = len(matrix[0])
        spiral_list=[]
        check = 1
        while flag!=0:
            
            if m==1 and check==0:
                flag=0
                map(spiral_list.append, list(matrix[::-1])[0])
                matrix = matrix[1:m]
            else:
                check=0
                map(spiral_list.append, list(matrix[0]))
                print matrix[0]
                matrix = matrix[1:m]
                rotated = zip(*matrix[::-1])
                rotated =zip(*rotated[::-1])
                matrix = zip(*rotated[::-1])
           
            m = len(matrix)
            if m==0 :
                flag = 0
            else:
                flag=1
                n = len(matrix[0])
            
            
        print spiral_list    
        return spiral_list    
