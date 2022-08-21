def partition(arr, leftIdx, rightIdx, way):
    pivot = arr[rightIdx]

    i = leftIdx - 1
    
    for j in range(leftIdx, rightIdx):
        if way == 'asc':
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        elif way == 'dsc':
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[rightIdx] = arr[rightIdx], arr[i+1]
    
    return i + 1

def quickSort(arr, leftIdx, rightIdx, way):
    if leftIdx < rightIdx:
        pi = partition(arr, leftIdx, rightIdx, way)
        quickSort(arr, leftIdx, pi - 1, way)
        quickSort(arr, pi + 1, rightIdx, way)

    return arr

if __name__ == "__main__":
    a = [9, -4, 1, -5, 3, -45, 0, 100]
    print(quickSort(a, 0, len(a)-1, 'asc'))
    print(quickSort(a, 0, len(a)-1, 'dsc'))