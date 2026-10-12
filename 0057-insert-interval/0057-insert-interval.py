class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      
        
        output=[]
        if not intervals:
            output.append(newInterval)
            return output

        for i in range(len( intervals)):
            st, ed=intervals[i]
            if st<newInterval[0]:
                output.append([st, ed])
            else:
                break


        print(output)
         
        
        if output and output[-1][1]>=newInterval[0]:
                s, e=output.pop()
                output.append([s,max(e,newInterval[1])])
                
        
        else:
            output.append(newInterval)

        
        while i<len(intervals):
            if output and output[-1][1]>=intervals[i][0]:

                s, e=output.pop()
                output.append([s,max(e,intervals[i][1])])
            else:
                output.append(intervals[i])

            i+=1
            


        

        return output

            

        
