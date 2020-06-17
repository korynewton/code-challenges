class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count= dict()
        #count elements of list
        for el in arr:
            if el in count:
                count[el] += 1
            else:
                count[el] = 1
        
        sorted_by_count = {key:value for key,value in sorted(count.items(), key=lambda x:x[1], reverse=True)}
        
        target = len(arr) / 2
        total_removed = unique_removed = 0
        for el in sorted_by_count:
            if (total_removed < target):
                total_removed += count[el]
                unique_removed += 1
            else:
                break
                
        return unique_removed
