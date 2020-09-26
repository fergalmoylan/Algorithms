from random import randint

#insertion sort

def insertionsort(lst):
    i = 1
    while i < len(lst):
        p = lst[i]
        j = i - 1
        while j >= 0 and p < lst[j]:
            lst[j+1] = lst[j]
            j -=1
        lst[j+1] = p

        i += 1

    return lst


def main():
    lst = []
    for i in range(randint(10, 35)):
        lst.append(randint(0, 100))
    print(insertionsort(lst))

if __name__ == '__main__':
    main()