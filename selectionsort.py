from random import randint

def selectionsort(lst):
    i = 0
    while i < len(lst):
        j = i + 1 # j goes through the list to find the smallest element
        p = i # p is the index of the smallest element
        while j < len(lst):
            if lst[j] < lst[p]: # if there's a new smallest element, put p at the index of it
                p = j
            j += 1
        lst[p], lst[i] = lst[i], lst[p] #put the smallest element at the start of the list
        i += 1

    return lst

def main():
    lst = []
    for i in range(randint(10, 50)):
        lst.append(randint(0, 100))
    
    print(selectionsort(lst))

if __name__ == '__main__':
    main()