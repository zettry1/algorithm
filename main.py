
class Solution:
    def rob(self, nums):
        prev1 = 0
        prev2 = 0
        for i in nums:
            temp = prev1
            prev1 = max(prev2+i,prev1)
            prev2 = temp
            print(i,prev1,prev2)
        return prev1


def moveZeroes(nums):
    idx=0
    for num in nums:
        if num!=0:
            nums[idx]=num
            idx+=1
    for i,num in enumerate(nums):
        if i>=idx:
            nums[i]=0


    print(nums,idx)

moveZeroes([0,1,0,3,15])

# solution = Solution()

# solution.rob([1,2,3,4,5])