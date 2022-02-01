class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total//2
        
        if len(a)>len(b):
            b, a = a, b
        
        l, r = 0, len(a)-1
        
        while True:
            i = (l+r)//2 #A
            j = half - i - 2 #B
            
            left_part_a = a[i] if i >=0 else float("-inf")
            right_part_a = a[i+1] if (i+1) <len(a) else float("inf")
            b_left = b[j] if j >= 0 else float ("-inf")
            b_right = b[j+1] if (j+1) < len(b) else float("inf")
            
            if left_part_a <= b_right and b_left <= right_part_a:
                if total % 2:
                    return min(right_part_a, b_right)
                return (max(left_part_a, b_left) + min(right_part_a, b_right))/2
            
            elif left_part_a > b_right:
                r = i-1
            else:
                l = i+1
        