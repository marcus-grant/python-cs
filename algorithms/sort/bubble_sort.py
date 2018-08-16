def bubble_sort(l):
    """ Sort list l using bubble sort algorithm """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                swapped = True
                tmp = l[i]
                l[i] = l[i+1]
                l[i+1] = tmp