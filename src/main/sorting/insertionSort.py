def insertionSort(arr, way):
   
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        if way == 'asc':
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        elif way == 'dsc':
            while j >= 0 and key > arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        
        arr[j+1] = key 

    return arr