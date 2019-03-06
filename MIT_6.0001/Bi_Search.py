def bisect_search1(L, e):
    """
        bisection search, recursive implementation
        L: list of numbers that are in ascending order
        e: number to search

        returns: Bool
    """
    if len(L) == 0:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)

def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if low == high:
            return L[low] == e
        if low > high:
            return False
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)

    return bisect_search_helper(L, e, 0, len(L)-1)

def test():
    L = [1,3,5,7,9,12,13,15,17,23,29,100,102,105]
    print(bisect_search2(L, 110))

test()

