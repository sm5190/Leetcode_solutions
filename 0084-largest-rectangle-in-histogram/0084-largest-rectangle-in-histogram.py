class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        # # Previous Smaller Element
        # def pse():
        #     res = [-1] * n
        #     stack = []
        #     for i in range(n):
        #         while stack and heights[stack[-1]] > heights[i]:
        #             stack.pop()
        #         res[i] = stack[-1] if stack else -1
        #         stack.append(i)
        #     return res

        # # Next Smaller Element
        # def nse():
        #     res = [n] * n
        #     stack = []
        #     for i in range(n-1, -1, -1):
        #         while stack and heights[stack[-1]] >= heights[i]:
        #             stack.pop()
        #         res[i] = stack[-1] if stack else n
        #         stack.append(i)
        #     return res

        # maxA=0
        # Pse=pse()
        # Nse=nse()
        # for i in range(len(heights)):
        #     area=heights[i]* (Nse[i]-Pse[i]-1)
        #     maxA=max(maxA, area)

        # return maxA
### Optimal
        st=[]
        nse=n
        pse=-1
        maxA=0
        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                element=heights[st[-1]]
                st.pop()
                nse=i
                pse=-1 if not st else st[-1]
                maxA=max((element*(nse-pse-1)), maxA)
            st.append(i)
        while st:
            nse=n
            element=heights[st.pop()]
            pse=-1 if not st else st[-1]
            maxA=max((element*(nse-pse-1)), maxA)

        return maxA



        
