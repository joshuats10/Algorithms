def selectionSort(arr, way):
    
    for i in range(len(arr)):
        idx = i

        for j in range(i+1, len(arr)):
            if way == 'asc':
                if arr[j] < arr[idx]:
                    idx = j
            elif way == 'dsc':
                if arr[j] > arr[idx]:
                    idx = j

        arr[i], arr[idx] = arr[idx], arr[i]
    
    return arr