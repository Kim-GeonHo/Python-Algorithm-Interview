from typing import List

class solution:
    def myself(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            result = 1
            for j in range(len(nums)):
                if i != j:
                    result *= nums[j]
        
            answer.append(result)

        return answer

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in range(len(nums))]
        
        prod = 1

        for i in range(len(nums) - 1):
            prod *= nums[i]
            answer[i+1] = prod

        prod = 1

        for i in range(len(nums) - 1):
            prod *= nums[len(nums) - i - 1]
            answer[len(nums) - i - 2] *= prod

        return answer

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]

        p = 1

        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] *= p
            p *= nums[i]
        
        return out

sol = solution()

nums = list(map(int, input().split()))

print(sol.myself(nums))
print(sol.productExceptSelf(nums))
print(sol.productExceptSelf2(nums))
