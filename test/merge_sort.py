def mergeSort(arr):
    if len(arr) > 1:
        # split the array into 2
        mid = len(arr) // 2
        arrayL = arr[:mid]
        arrayR = arr[mid:]

        mergeSort(arrayL)
        mergeSort(arrayR)

        # initialize array indicies
        i = 0
        j = 0
        k = 0

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

toSort = []

def getArrayLength():
    try:
        n = int(input("Input the amount of entries in the array to sort with Merge Sort: "))
    except ValueError:
        print("Value is not a valid integer.")
        getArrayLength()
    else:
        if n > 1:
            getArrayValues(n)
        else:
            print("Value is not applicable for sorting.")
            getArrayLength()

def getArrayValues(arrayLength: int):
    inserted = 0
    while inserted < arrayLength:
        try:
            value = int(input(f"Input a number ({inserted + 1}/{arrayLength}): "))
            toSort.append(value)
        except ValueError:
            print("Value is not a valid integer.")
        else:
            inserted += 1

def main():
    getArrayLength()
    print(f"Before sorting: {toSort}")
    mergeSort(toSort)
    print(f"After sorting: {toSort}")

if __name__ == "__main__":
    main()