'''
202: Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while (n!=1):
            n = sum(int(digit) ** 2 for digit in str(n))
            if n in seen: # Cycle detected
                return False
            seen.add(n)

        return True # No cycle detected

if __name__ == "__main__":
    # Test cases#+¯
    test_cases = [19, 2, 7, 1, 100]

    solution = Solution()#+¯
    for num in test_cases:
        result = solution.isHappy(num)
        print(f"Input: {num}, Output: {result}")
