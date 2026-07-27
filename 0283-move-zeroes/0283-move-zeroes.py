class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        nums1= []
        for i in range(len(nums)):
            if nums[i] != 0:
                nums1.append(nums[i])
            else:
                count+=1
        for i in range(count):
            nums1.append(0)
        for i in range(len(nums1)):
            nums[i] = nums1[i]
                

        
        