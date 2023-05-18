def mergeSort(arr):
    if len(arr) > 1:
        # split the array into 2
        mid = len(arr) // 2
        arrayL = arr[:mid]
        arrayR = arr[mid:]

        mergeSort(arrayL)
        mergeSort(arrayR)

        i = j = k = 0

        # combining the halves back
        while i < len(arrayL) and j < len(arrayR):
            if arrayL[i] < arrayR[j]:
                arr[k] = arrayL[i]
                i += 1
            else:
                arr[k] = arrayR[j]
                j += 1
            k += 1
        
        # pick up leftover values
        while i < len(arrayL):
            arr[k] = arrayL[i]
            i += 1
            k += 1
        
        while j < len(arrayR):
            arr[k] = arrayR[j]
            j += 1
            k += 1

exampleArray = [6, 5, 3, 1, 8, 7, 2, 4]
print(f"Initial array: {exampleArray}")
mergeSort(exampleArray)
print(f"Sorted array: {exampleArray}")