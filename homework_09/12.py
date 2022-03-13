def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


#class_1 = []
#class_2 = []

class_1 = [elem for elem in range(160, 177, 2)]
class_2 = [elem for elem in range(162, 181, 3)]
#for i in range(160, 177, 2):
#    class_1.append(i)
#for j in range(162, 181, 3):
#    class_2.append(j)
#class_join = [*class_1, *class_2]
class_join = [i for i in (class_1 or class_2)]
#class_join = [i for i in class_1] or [j for j in class_2]
selection_sort(class_join)
#class_join.sort()
print(class_join)
