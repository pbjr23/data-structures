def build_max_heap(l, type_of_heap):
    """Takes a list as input and builds a heap out of it
       0 = maxheap
       1 = minheap"""
    h.list = l
    h.heapsize = len(l)
    for i in range(len(l)/2-1, -1, -1):
        h.max_heapify(i)
    return h


class MaxHeap(object):
    """Python min/max heap representation"""

    def __init__(self, l=[]):
        """Initializes the heap
        Accepted entries:
        m = Heap() <-> Creates an empty max heap
        m = Heap([1,2,3]) <-> Turns the input list into a maxheap
        """
        if (not isinstance(l, list)) and (not all(isinstance(element, (int, long, float)) for element in l)) and l != []:
          raise Exception("Invalid format given")
        self.list = l
        self.heapsize = len(l)

    def __str__(self):
        """Prints out the matrix as a string, without any brackets around it
        Format: 1 2 <-> print Matrix([[1, 2], [3, 4]])
        3 4
        """
        return '[' + ', '.join([str(element) for element in self.list]) + ']' 

    def append(self, input):
        """Inserts a new element into the heap
        """
        self.list.append(-float("inf"))
        self.heap_increase_key(self.heapsize, input)
        self.heapsize += 1

    def max_heapify(self, index):
        """Note: index starts from 0 in this representation """
        try:
            left = 2*index + 1
            right = 2*index + 2
            largest = index
            if self.list[left] > self.list[index]:
                largest = left
            if self.list[right] > self.list[largest]:
                largest = right
            if largest != index:
                temp = self.list[index]
                self.list[index] = self.list[largest]
                self.list[largest] = temp
                self.max_heapify(largest)
        except IndexError:
            return

    def heap_increase_key(self, index, new_key):
        if new_key < self.list[index]:
            raise Exception("Invalid input: new_key must be greater than current index value")
        self.list[index] = new_key
        while index > 0 and self.list[index] > self.list[(index-1)/2]:
            temp = self.list[(index-1)/2]
            self.list[(index-1)/2] = self.list[index]
            self.list[index] = temp
            index = (index - 1)/2

    def __eq__(self, other):
        """ == Checks if two heaps are equal."""
        return self.list == other.list and self.type == other.type

    def __ne__(self, other):
        """!= Check if two heaps are not equal."""
        return not self.__eq__(other)


h = MaxHeap()
h.append(1)
h.append(4)
h.append(6)
h.append(1)
h.append(4)
h.append(3)
h.append(3)
# print h
# h.max_heapify(0)
# print h

h.list = [7, 5, 6, 4, 2, 1, 3]
# print h
h.heap_increase_key(6,10)
print h
h.append(9)
print h
# l = buildheap([1, 2, 3, 4, 5, 6, 7], 0)
# print l

