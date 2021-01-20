from typing import List

class solution:
    def my_self(self, height: List[int]) -> int:
        volume = 0
        max_height = max(height)

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0

        max_index = height.index(max_height)

        while (left != max_index):
            if (height[left] > left_max):
                left_max = height[left]
            else:
                volume += left_max - height[left]

            left += 1

        while (right != max_index):
            if(height[right] > right_max):
                right_max = height[right]
            else:
                volume += right_max - height[right]

            right -= 1

        return volume

    def two_pointer(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

    def stack(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):

            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[stack[-1]], height[i]) - height[top]

                volume += distance * waters

            stack.append(i)

        return volume

sol = solution()

height = list(map(int, input().split()))

print(sol.my_self(height))
print(sol.two_pointer(height))
print(sol.stack(height))
