def bubbleSort(arr, way):
    
    for i in range(len(arr)):
        
        swapped = False
        
        for j in range(0, len(arr) - i - 1):
            if way == 'asc':
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            elif way == 'dsc':
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True

        if not swapped:
            break

    return arr