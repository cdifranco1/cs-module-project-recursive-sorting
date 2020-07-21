# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    """
    Crete pointer to arrA and arrB
    Iterate range of length merged_arr
    for each iteration:
        if arrA[pointerA] > arrB[pointerB]:
            mergedArr[i] = arrA[pointerA]
            pointerA += 1
        else:
            mergedArr[i] = arrB[pointerB]
            pointerB += 1
    """
    # Your code here
    idx1 = 0
    idx2 = 0
    for i in range(len(merged_arr)):
        if idx1 > len(arrA) - 1:
            merged_arr[i] = arrB[idx2]
            idx2 += 1
        elif idx2 > len(arrB) - 1:
            merged_arr[i] = arrA[idx1]
            idx1 += 1
        elif arrA[idx1] < arrB[idx2]:
            merged_arr[i] = arrA[idx1]
            idx1 += 1
        else:
            merged_arr[i] = arrB[idx2]
            idx2 += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:len(arr)]
    
    arr = merge(merge_sort(left), merge_sort(right))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # left = arr[start:mid]
    # right = arr[mid:end]

    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

arr1 = [12, 3, 4, 5, 1, 0, -9]
print(merge_sort(arr1))