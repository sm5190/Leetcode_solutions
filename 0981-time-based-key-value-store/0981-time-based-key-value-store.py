class TimeMap:

    def __init__(self):
        self.times={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key]=[]
        self.times[key].append([timestamp,value])

        
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        # if timestamp< self.times[key][0][0]:
        #     return ""

        left=0
        right=len(self.times[key])-1
        res=""
        while left<=right:

            mid =(left+right)//2

            if self.times[key][mid][0]<=timestamp:
                res=self.times[key][mid][1]
                left=mid+1
            else:
                right=mid-1

        return res

     

                    
                    

        



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)