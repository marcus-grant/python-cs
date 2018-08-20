def binary_search_nearest(l, val):
    # Set the search interval from start to end of l
    left = 0
    right = len(l) - 1

    # Keep iterating till left is next to right indexes
    while (right - left) > 1:
        # Find the middle location and value
        mid = (right + left) >> 1 # TODO: avg without overflow
        mid_val = l[mid]
        # If the search val is bigger, refocus the search on the right side
        if mid_val < val:
            left = mid
        # If search val is smaller, refocus search on left side
        elif mid_val > val:
            right = mid
        # If equal then it's done
        else:
            return mid
    
    # Now that the left/right indices are adjacent, --
    # return the index with the value nearest the search val
    mid_val = (l[right] / 2) + (l[left] / 2)
    if mid_val <= val:
        return right
    return left