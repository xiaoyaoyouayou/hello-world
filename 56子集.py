# #每日一题 No.56
#
# 子集
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
#
# 示例:
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#
# 链接：https://leetcode-cn.com/problems/subsets/




def func(nums):
    res=[[]]
    for i in nums:
        res=res+[[i]+num for num in res]
    return res
print(func([1,2,3]))


class Solution:
    def subsets(self, nums):
        res=[[]]
        for i in nums:
            res=res+[[i]+num for num in res]
        return res

import itertools
class Solution:
    def subsets(self, nums):
        res=[]
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums,i):
                res.append(tmp)
        return res
c=Solution()
print(c.subsets([1,2,3]))