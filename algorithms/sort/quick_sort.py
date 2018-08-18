from . import insertion_sort

def median_three(l, lo, hi):
    """ Takes a list, and start/end indicies and
        uses them to find the median 
    """
    # There are a few edge cases that need different treatment.
    # In the larger context, this function will get called till lo >= hi
    # Therefore we need a few edge cases for differences of lo - high < 2
    if (hi - lo) < 2:
        if l[lo] > l[hi]:
            l[lo], l[hi] = l[hi], l[lo]
        return l[lo]
    
    # Compute the middle index.
    # It's a way of doing it avoiding overflow and faster due to bitwise math
    mid = (lo + (hi - 1)) >> 1

    # An unrolled sort that places the correct values in median of three order
    if l[lo] > l[hi]:
        l[lo], l[hi] = l[hi], l[lo]
    if l[lo] > l[mid]:
        l[lo], l[mid] = l[mid], l[lo]
    if l[mid] > l[hi]:
        l[mid], l[hi] = l[hi], l[mid]
    
    # return the middle index for use by partitioner
    return l[mid]

def partition_median3(l, lo, hi):
    """ Performs quick sort partitioning, here it uses median of three
        as the pivot selection process, which sorts the three so the pivot
        becomes the middle element of those three sorted elements.
    """
    # Get the pivot value
    pivot_val = median_three(l, lo, hi)

    # Initialize the hi-side & lo-side crawlers.
    # Because median_three already sorts the lo/hi indicices, skip them.
    lo_crawler = lo + 1
    hi_crawler = hi - 1

    # Setup the outer loop of the partitioner
    while True:
        # Increment lo crawler till a value greater than pivot.
        while l[lo_crawler] < pivot_val:
            lo_crawler += 1
        
        # Increment hi crawler till a value lower than pivot.
        while l[hi_crawler] > pivot_val:
            hi_crawler -= 1
        
        # If the crawlers have met or crossed each other, then...
        # ...done crawling partition and swapping unordered elements.
        if lo_crawler >= hi_crawler:
            return hi_crawler
        
        # Otherwise swap the current elements and continue crawlers with loop
        l[lo_crawler], l[hi_crawler] = l[hi_crawler], l[lo_crawler]

        # Because it's possible that after a swap occurs, the crawlers...
        # ...can get stuck, need to move the crawlers before proceeding.
        lo_crawler += 1
        hi_crawler -= 1

def quick_sort_recurser_median3(l, lo, hi):
    # Continue recursion unless the intervels have met or passed each other.
    if lo >= hi:
        return
    
    # Now partition the current interval around a pivot.
    # Everything before the pivot is smaller, after is higher.
    # Get the partition index to use in recursing into each partition.
    partition_idx = partition_median3(l, lo, hi)
    quick_sort_recurser_median3(l, lo, partition_idx)
    quick_sort_recurser_median3(l, partition_idx + 1, hi)

def quick_sort_recurser_insertion(l, lo, hi, cutoff):
    """ Performs quick sort until a partition size <= cutoff
        is reached, where it will switch to insertion sort.
    """
    # If the cutoff is reached, finish sorting partition with insertion sort
    if (hi - lo) < cutoff:
        insertion_sort.insertion_sort(l, lo=lo, hi=hi)
        return
    
    # Now partition the current interval around a pivot.
    # Everything before the pivot is smaller, after is higher.
    # Get the partition index to use in recursing into each partition.
    partition_idx = partition_median3(l, lo, hi)
    quick_sort_recurser_insertion(l, lo, partition_idx, cutoff)
    quick_sort_recurser_insertion(l, partition_idx + 1, hi, cutoff)

def partition_simple(l, lo, hi):
    """ A basic version of quick sort partition that simply chooses
        the middle value in a partition and partitions values so
        lower than the middle value goes to the beginning and opposite to end
    """
    # Set the pivot index to be the middle index
    mid = (lo + (hi - 1)) >> 1
    pivot_val = l[mid]

    # Set up the crawlers that swap values on wrong side of pivot
    lo_crawler = lo
    hi_crawler = hi

    # Crawl the list on both sides, swapping when lo > hi.
    while True:
        # Crawl on low side till a value greater than pivot is reached
        while l[lo_crawler] < pivot_val:
            lo_crawler += 1
        
        # Crawl on hi side till a value lower than pivot is reached
        while l[hi_crawler] > pivot_val:
            hi_crawler -= 1
        
        # Check that the crawlers haven't passed each other and stop crawling
        if lo_crawler >= hi_crawler:
            return hi_crawler
        
        # Swap the references to partition in order
        l[lo_crawler], l[hi_crawler] = l[hi_crawler], l[lo_crawler]

        # Move the crawlers to continue.
        # Not doing this wastes comparisons and risks infinite loops if
        # the remaining partition has values equal to pivot
        lo_crawler += 1
        hi_crawler -= 1

def quick_sort_recurser_simple(l, lo, hi):
    """ Recursive quick sort function that uses a simple, pivot selection
        of just picking the middle value every time.
    """
    # If the partitions have become 1 element or none, stop recursing
    if lo >= hi:
        return
    
    # Partition then recurse
    partition_idx = partition_simple(l, lo, hi)
    quick_sort_recurser_simple(l, lo, partition_idx)
    quick_sort_recurser_simple(l, partition_idx + 1, hi)


def quick_sort(l, algorithm='median3', cutoff=7):
    """ Sets up the various quick_sort algorithms to perform a quick sort.
        Takes a conditional argument 'algorithm' to choose which variant
        of quick sort to chose from, defaults to median of three
    """
    hi = len(l) - 1
    if algorithm == 'median3':
        quick_sort_recurser_median3(l, 0, hi)
    elif algorithm == 'insert':
        quick_sort_recurser_insertion(l, 0, hi, cutoff)
    elif algorithm == 'simple':
        quick_sort_recurser_simple(l, 0, hi)
    return