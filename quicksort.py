from random import randint

def quicksort(lst):
    if len(lst) <=1:
        return lst
    else:
        p = lst.pop()

    hi = []
    lo = []
    for item in lst:
        if item > p:
            hi.append(item)
        else:
            lo.append(item)
    return quicksort(lo) + [p] + quicksort(hi)

def main():
    lst = []
    for i in range(randint(10, 35)):
        lst.append(randint(0, 100))
    print(quicksort(lst))

if __name__ == '__main__':
    main()