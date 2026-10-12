class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        starts=[]
        ends=[]
        for i in range(len(intervals)):
            starts.append(intervals[i][0])
            ends.append(intervals[i][1])
        
        starts.sort()
        ends.sort()
        print(ends)
        print(starts)
        ans=[]
        i=0
        while i<len(starts):
            if ans and starts[i]<=ans[-1][1] :
                x=ans[-1][0]
                ans.pop()
                
                ans.append([x, ends[i]])
                

                
            else:
                ans.append([starts[i],ends[i]] )
                
            i=i+1


        return ans