"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].



Using new logic, with for loop and if else statements, find the target number in the list and print the index of the target number if found, else print a message that the target number is not found in the list.
"""


class solution:
    def __init__(self, nums, target):
        arr = []
        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)

        
        if(arr):
            print(arr)
        else:
            print("[-1, -1]")
        
   

             





def main():
    nums = [66,44,23,76,84,66,90]
    target = int(input("Enter your target number: "))
    sol = solution(nums, target)


if __name__ == "__main__":
   main()