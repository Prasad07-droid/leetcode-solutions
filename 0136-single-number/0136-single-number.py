class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for x in nums:
          count[x] = count.get(x,0) + 1
        for key, value in count.items():
            if value == 1:
                return key

         
            
        