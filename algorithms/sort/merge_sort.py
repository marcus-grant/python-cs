def merge(lst, start, mid, end):
    """ Merge function for merge sort that merges
        the sub-lists of 'lst' from 'start' to 'end',
        segregated by the 'mid' index.
    """
    # Setup temp list
    tmp_list = [0] * (end - start + 1)

    # Setup crawler indices for both intervals being merged
    first_crawler = start
    second_crawler = mid + 1
    tmp_idx = 0 # ...and for the tmp_list where merger resolves

    # Traverse both intervals simultaneously & the tmp_list,
    # placing the lowest from each interval into tmp_list.
    while first_crawler <= mid and second_crawler <= end:
        first_val = lst[first_crawler]
        second_val = lst[second_crawler]
        # if the first interval has a smaller value add it
        if first_val <= second_val:
            tmp_list[tmp_idx] = first_val
            first_crawler += 1
        else:
            tmp_list[tmp_idx] = second_val
            second_crawler += 1
        tmp_idx += 1 # don't forget to increment k's crawler
    
    # Since one crawler could've stopped early,
    # go through each of them till the end to add remainder to tmp_lst
    while first_crawler <= mid:
        tmp_list[tmp_idx] = lst[first_crawler]
        first_crawler += 1
        tmp_idx += 1

    while second_crawler <= end:
        tmp_list[tmp_idx] = lst[second_crawler]
        second_crawler += 1
        tmp_idx += 1
    
    # Finally, copy tmp_idx back into original list at given interval
    for tmp_idx in range(end - start + 1):
        lst[tmp_idx + start] = tmp_list[tmp_idx]

def merge_sort_recursive(l, start, end):
    """ The recursive part of merge_sort.
        Finds the middle point to split the sort.
        Then Calls itself on the first half.
        Same for the second half.
        Merges current part.
        This recursion means the smallest possible partitions
        get merged into sorted sub-lists.
        Each recursion depth upward goes towards the final size,
        with each recursion below having sorted sublists.
        After the final merger, the list is sorted.
    """
    # The final recursion occurs when start & end are the same.
    # If this is the case there's nothing to merge, so continue in above call.
    if start >= end:
        return
    
    # Figure out the mid point before partitioning recursively.
    # The minus 1 in parentheses is to avoid overflow and to normalize range.
    # The >> 1 is a quick way to divide by 2**1 using bitwise math.
    mid = (start + (end - 1)) >> 1

    # Partition into two sections around mid, then merge them.
    # When done recursively the smallest partitions are merged first.
    # Then the previous level of recursion does this to a larger partition.
    merge_sort_recursive(l, start, mid)
    merge_sort_recursive(l, mid + 1, end)
    merge(l, start, mid, end)

    

def merge_sort(l):
    """ Sort with merge sort algorithm.
        This calls the function that does the actual recursion & merging,
        merge_sort_recursive().
        This way, a clean function signature is exposed to developers.
    """
    merge_sort_recursive(l, 0, len(l) - 1)


# def recursive_merge_sort(lst, ):