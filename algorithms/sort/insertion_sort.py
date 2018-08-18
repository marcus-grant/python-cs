def insertion_sort(l, lo=0, hi=None):
    if hi is None:
        hi = len(l) - 1
    i = 1
    while i <= hi:
        val = l[i]
        j = i - 1
        while j >= 0 and l[j] > val:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = val
        i += 1