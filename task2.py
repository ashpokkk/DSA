"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].

Using Binary Search Logic
"""
from operator import index


class solution:
    def __init__(self, nums, target):
     self.nums = nums
     self.target = target
     low = 0
     high = len (nums) - 1
     while low<=high:
       mid = (low + high) // 2
       if self.target  ==  nums[mid]:
        print ("Target number found at index:", nums.index(target))
        break
       elif self.target < nums[mid]:
          high = mid - 1
       elif self.target > nums[mid]:
          low = mid + 1
         




def main():
    nums = [2,2,3,4,4,4,5,6,6,7,8]
    target = int(input("Enter your target number:"))
    sol = solution(nums, target)




if __name__ == "__main__":
    main()