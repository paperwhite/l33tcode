class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        final_list = []
        j=0
        k=0
        flag=1
        check=1
        if len(nums1)==0:
            final_list=nums2
            check=0
        if len(nums2)==0:
            final_list=nums1
            check=0
            
        while flag==1 and check!=0:
             
            if nums1[k] > nums2[j]:
                final_list.append(nums2[j])
                j=j+1
            elif nums1[k] < nums2[j]:
                final_list.append(nums1[k])
                k=k+1
            else:
                final_list.append(nums1[k])
                k=k+1
                final_list.append(nums2[j])
                j=j+1
            
            if k == len(nums1) or j ==len(nums2):
                if k >= len(nums1):
                    final_list.extend(nums2[j:])
                if j >= len(nums2):
                    final_list.extend(nums1[k:])
                flag=0
        
        l = len(final_list)
        if l%2==1:
            return final_list[int(math.floor(l/2))]
        else:
            
            return (final_list[int(math.floor(l/2))]+final_list[int(math.floor(l/2))-1])/float(2)
