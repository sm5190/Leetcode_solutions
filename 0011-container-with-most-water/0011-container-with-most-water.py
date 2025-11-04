class Solution:
    def maxArea(self, height: List[int]) -> int:

        i=0
        j=len(height)-1
        max1=0
        while i<j:
            h= min(height[i],height[j])
            max1=max( max1, (j-i)* h)
                
            if height[i]< height[j]:
                i=i+1
            elif height[j]< height[i]:
                j=j-1
            else:
                i=i+1
            
            
                
        print(i,j)  
        return max1