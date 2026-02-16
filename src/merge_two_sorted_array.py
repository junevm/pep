# merge two sorted array
def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i, j = 0, 0

    # Traverse both arrays and append the smaller element to merged_array
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # If there are remaining elements in arr1, append them
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # If there are remaining elements in arr2, append them
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array