'''
189 Medium: Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Handle cases where k is larger than the array length
        nums[:] = nums[-k:] + nums[:-k]  # Efficiently rotate the array in-place

        
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    solution.rotate(nums1, k1)
    print(f"Test case 1: {nums1}")  # Expected: [5, 6, 7, 1, 2, 3, 4]
    
    # Test case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    solution.rotate(nums2, k2)
    print(f"Test case 2: {nums2}")  # Expected: [3, 99, -1, -100]