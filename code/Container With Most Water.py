class Solution:
    def maxArea(self, height):
        max_area = 0
        a_pointer = 0
        b_pointer = len(height) - 1

        while a_pointer < b_pointer:
            if height[a_pointer] < height[b_pointer]:
                max_area = max(max_area, height[a_pointer] * (b_pointer - a_pointer))
                a_pointer += 1
            else:
                max_area = max(max_area, height[b_pointer] * (b_pointer - a_pointer)) 
                b_pointer -= 1
        
        return max_area
# Runtime: 700 ms, faster than 78.12% of Python3 online submissions for Container With Most Water.
# Memory Usage: 26.6 MB, less than 69.78% of Python3 online submissions for Container With Most Water.


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    sol = Solution.maxArea(Solution, height)
    print(sol)
        

