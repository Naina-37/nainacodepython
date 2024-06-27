print("~~~~~~~~~~~~~~~~~~~~~~~~~~~BUBBLE SORT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def bubble_sort(data):
    for  i in range(0, len(data)-1):
        print("i is:",i)
        for j in range(len(data)-i-1):
            print(j, end="")
            if data[j]>data[j+1]:
                #swap operation
                data[j],data[j+1]=data[j+1],data[j]
                print()


numbers=[10,30,50,80,40]
bubble_sort(numbers)
print("unsorted numbers")
print(numbers)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("sorted numbers:")
print(numbers)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")