'''
191. Number of 1 Bits

Given a positive integer n, write a function that returns the number of set bits in its binary representation 
(also known as the Hamming weight).

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

Constraints:

1 <= n <= 231 - 1
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # Increment count if the least significant bit is 1
            count += n & 1
            # Right-shift n by 1 to check the next bit
            n >>= 1
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingWeight(11))  # Expected output: 3
    print(solution.hammingWeight(128))  # Expected output: 1
    print(solution.hammingWeight(2147483645))  # Expected output: 30