from typing import List

class solution:
    def myself(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0

        for i in range(0, len(nums), 2):
            sum += nums[i]
        
        return sum

    def ascending(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

sol = solution()

nums = list(map(int, input().split()))

print(sol.myself(nums))
print(sol.ascending(nums))
