class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def DFS(nums,path):
            if not nums:
                # append path to result array when num is empty
                result.append(path)
            for i in range(len(nums)):
                #all nums execpt num at i
                others = nums[:i] + nums[i+1:]
                #recursively call DFS for all nums adding one additional num to path each call
                DFS(others, path+[nums[i]])
                
        DFS(nums,[])
        
        return result
      
