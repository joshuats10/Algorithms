def mergeSort(arr, way):

    if len(arr) > 1:
        r = len(arr) // 2
        sub1 = arr[:r]
        sub2 = arr[r:]

        mergeSort(sub1, way)
        mergeSort(sub2, way)

        i = j = k = 0

        while i < len(sub1) and j < len(sub2):
            if way == 'asc':
                if sub1[i] < sub2[j]:
                    arr[k] = sub1[i]
                    i += 1
                else:
                    arr[k] = sub2[j]
                    j += 1
                k += 1
            elif way == 'dsc':
                if sub1[i] > sub2[j]:
                    arr[k] = sub1[i]
                    i += 1
                else:
                    arr[k] = sub2[j]
                    j += 1
                k += 1

        while i < len(sub1):
            arr[k] = sub1[i]
            i += 1
            k += 1

        while j < len(sub2):
            arr[k] = sub2[j]
            j += 1
            k += 1

    return arr