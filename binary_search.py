import time
from pprint import pprint


# рекурсия
def bin_search_r(list_, high, item, low=0):
    if high >= low:

        mid = (low + high) // 2
        guess = list_[mid]

        if guess == item:
            return mid
        elif guess > item:
            return bin_search(list_, high=mid - 1, item=item, low=low)
        else:
            return bin_search(list_, low=mid + 1, high=high, item=item)
    else:
        return None


def bin_search_d(list_, max_, item, min_=0):
    while max_ >= min_:

        mid = (min_ + max_) // 2
        guess = list_[mid]

        if guess == item:
            return mid
        elif guess > item:
            max_ = mid - 1
        else:
            min_ = mid + 1
    return None


def main():
    s = time.time()

    arr_ = range(1, 1999999999999999999)
    print(bin_search_d(item=1999999999999999998, list_=list_, max_=len(arr_) - 1))
    
    print(f'Бинарный поиск: {time.time() - s}')


if __name__ == '__main__':
    main()
