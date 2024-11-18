'''
260 Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
 

Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
'''

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: Find the XOR of all numbers
        xor_result = 0
        for num in nums:
            xor_result ^= num

        # Step 2: Find the rightmost set bit in xor_result
        rightmost_set_bit = xor_result & -xor_result

        # Step 3: Divide the numbers into two groups and find the unique numbers
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num  # Group with the set bit
            else:
                num2 ^= num  # Group without the set bit

        return [num1, num2]

# Main function to test the solution
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 1, 3, 2, 5],  # Output: [3, 5] or [5, 3]
        [-1, 0],            # Output: [-1, 0] or [0, -1]
        [0, 1],             # Output: [1, 0] or [0, 1]
    ]
    
    solution = Solution()
    for nums in test_cases:
        result = solution.singleNumber(nums)
        print(f"Input: {nums}, Output: {result}")
