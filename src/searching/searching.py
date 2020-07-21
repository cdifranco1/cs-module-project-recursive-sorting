# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start > end:
        return -1
        
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        end = mid - 1
        return binary_search(arr, target, start, end)
    else:
        start = mid + 1
        return binary_search(arr, target, start, end)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # start = arr[0]
    # end = len(arr) - 1

    # if start < end:
    #     while start <= end:
    #         mid = (start + end) // 2
    #         if arr[mid] == target:
    #             return mid




arr1 = [1, 3, 5, 6, 12, 20, 34]
arr1 = sorted(arr1)



print(binary_search(arr1, 0, 0, len(arr1) - 1))