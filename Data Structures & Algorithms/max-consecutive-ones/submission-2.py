class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ls = [str(x) for x in nums]
        str_nums = "".join(ls)
        res=[]
        for i in str_nums.split("0"):
            res.append(len(i))

        return(max(res))
