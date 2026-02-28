class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
    
        ans=[0]* len(temperatures)
        for i, t in enumerate(temperatures):
            while st and t> temperatures[st[-1]]:
                ind=st.pop()
                ans[ind]=(i-ind)

            st.append(i)

        return ans
            