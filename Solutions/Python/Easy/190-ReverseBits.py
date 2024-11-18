'''
Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Constraints:

The input must be a binary string of length 32
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):  # Iterate through all 32 bits
            # Get the least significant bit of n
            bit = n & 1
            # Shift result to the left to make room for the new bit
            result = (result << 1) | bit
            # Shift n to the right to process the next bit
            n >>= 1
        return result

if __name__ == "__main__":
    solution = Solution()
    # Test cases
    print(solution.reverseBits(43261596))  # Expected output: 964176192
    print(solution.reverseBits(4294967293))  # Expected output: 3221225471
