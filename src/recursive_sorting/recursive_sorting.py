# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    A_index = 0
    B_index = 0
    # Your code here
    for i in merged_arr:
        if(arrA[A_index] < arrB[B_index]):
            merged_arr.append(arrA[A_index])
            A_index+1
        else:
            merged_arr.append(arrB[B_index])
            B_index+1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    start = 0
    end = len(arr)-1
    mid = end // 2

    #base case
    if(start == end):
        return arr

    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
