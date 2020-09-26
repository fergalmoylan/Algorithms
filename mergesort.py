from random import randint

def mergesort(lst):
    # """
    # lst of numbers is taken as input, and is split into two halves, following which they are recursively sorted.
    # """
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2     # note: 7//2 = 3, whereas 7/2 = 3.5

    left_lst = mergesort(lst[:mid])
    right_lst = mergesort(lst[mid:])

    return merge(left_lst, right_lst)

def merge(left, right):
    # """
    # Traverse both sorted sub-arrays (left and right), and populate the result array
    # """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result


def main():
    lst = []
    for i in range(randint(5, 8)):
        lst.append(randint(0, 100))
    print(mergesort(lst))


if __name__ == '__main__':
    main()    print(lst)