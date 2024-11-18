'''
258 Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
'''

class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            num = sum(int(digit) for digit in str(num))
        return num
if __name__ == "__main__":
    # Test cases
    test_cases = [38, 0, 9, 123, 4567]

    solution = Solution()
    for num in test_cases:
        result = solution.addDigits(num)
        print(f"Input: {num}, Output: {result}")