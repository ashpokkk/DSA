"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].



 solving this with WHILE loop and if else statements with my old logic.
"""


class solution:
    def __init__(self, nums, target):
       count = 0
       status = False
       while count < len(nums):
         if nums[count] == target:
           print(f"Target number {target} found at index [{count}] ")
           status = True
         count  = count+1
        

       if not status:
            print(f"Target number {target} not found in the list [1, -1]")
        
   

             





def main():
    nums = [66,44,23,76,84,66,90]
    target = int(input("Enter your target number: "))
    sol = solution(nums, target)


if __name__ == "__main__":
   main()