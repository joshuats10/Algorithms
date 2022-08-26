"""
    Indexed Priority Queue data structure implementation

    @author Joshua Teguh Santoso, joshuateguhsantoso@gmail.com
"""

class indexedPQ:
    def __init__(self, size):
        self.val = [None] * size
        self.pm = [None] * size
        self.im = [None] * size
        self.sz = 0

    def size(self):
        return self.sz

    def isEmpty(self):
        return self.sz == 0

    def contains(self, ki):
        return self.pm[ki] is not None

    def insert(self, ki,  val):
        self.val[ki] = val
        self.pm[ki] = self.sz
        self.im[self.sz] = ki

        self.__swim(self.sz)
        self.sz += 1

    def remove(self, ki):
        i = self.pm[ki]
        self.sz -= 1
        self.__swap(i, self.sz)

        self.__sink(i)
        self.__swim(i)

        self.val[ki] = None
        self.pm[ki] = None
        self.im[self.sz] = None

    def poll(self):
        ret_ki = self.im[0]
        ret_val = self.val[ret_ki]
        self.remove(ret_ki)

        return ret_ki, ret_val

    def update(self, ki, val):
        i = self.pm[ki]
        self.val[ki] = val
        self.__sink(i)
        self.__swim(i)

    def decreaseKey(self, ki, val):
        if self.__compareLess(val, self.val[ki]):
            self.val[ki] = val
            self.__swim(self.pm[ki])

    def increaseKey(self, ki, val):
        if self.__compareLess(self.val[ki], val):
            self.val[ki] = val
            self.__sink(self.pm[ki])

    def __swap(self, i, j):
        self.pm[self.im[j]], self.pm[self.im[i]] = i, j
        self.im[i], self.im[j] = self.im[j], self.im[i]

    def __less(self, i, j):
        return self.val[self.im[i]] < self.val[self.im[j]]

    def __compareLess(self, val_i, val_j):
        return val_i < val_j
    
    def __swim(self, i):
        parent = (i-1)//2
        while i > 0 and self.__less(i, parent):
            self.__swap(i, parent)
            i = parent
            parent = (i-1)//2

    def __sink(self, i):

        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = left

            if right < self.sz and self.__less(right, left):
                smallest = right
            
            if left >= self.sz or self.__less(i, smallest):
                break

            self.__swap(smallest, i)
            i = smallest