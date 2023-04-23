def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

sorted_list = selection_sort(my_list)  

print(sorted_list)

def binary_search(item, lst):
    first = 0
    last = len(lst) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    if found:
        print(f"{item} found at index {midpoint}")
    else:
        print(f"{item} not found in the list")

my_list = [1, 3, 5, 7, 9]

binary_search(3, my_list)  # will print "3 found at index 1"

binary_search(4, my_list)  # will print "4 not found in the list"

