def buildheap(l, type_of_heap):
    """Takes a list as input and builds a heap out of it
       0 = maxheap
       1 = minheap"""
    h = Heap(type_of_heap)
    h.list = l
    h.heapsize = len(l)
    for i in range(len(l)/2, -1, -1):
        h.heapify(i)
    return h

class Heap(object):
    """Python min/max heap representation"""

    def __init__(self, type_of_heap):
        """Initializes the heap
        Accepted entries:
        mmax = Heap(0) <-> Creates a max heap
        mmin = Heap(1) <-> Creates a min heap
        """
        self.type = type_of_heap
        self.list = []
        self.heapsize = 0
        if type_of_heap != 0 and type_of_heap != 1:
            raise Exception("Invalid format given")

    def __str__(self):
        """Prints out the matrix as a string, without any brackets around it
        Format: 1 2 <-> print Matrix([[1, 2], [3, 4]])
        3 4
        """
        return '[' + ', '.join([str(element) for element in self.list]) + ']' 

    def append(self, input):
        """Prints out the matrix as a string, without any brackets around it
        Format: 1 2 <-> print Matrix([[1, 2], [3, 4]])
        3 4
        """
        self.list.append(input)

    def heapify(self, index):
        """Note: index starts from 0 in this representation """
        if self.type == 0:
            try:
                left = 2*index + 1
                right = 2*index + 2
                largest = index
                if self.list[left] > self.list[index]:
                    largest = left
                if self.list[right] > self.list[index]:
                    largest = right
                if largest != index:
                    temp = self.list[index]
                    self.list[index] = self.list[largest]
                    self.list[largest] = temp
                    self.heapify(largest)
            except IndexError:
                return
        if self.type == 1:
            try:
                left = 2*index + 1
                right = 2*index + 2
                largest = index
                if self.list[left] < self.list[index]:
                    largest = left
                if self.list[right] < self.list[index]:
                    largest = right
                if largest != index:
                    temp = self.list[index]
                    self.list[index] = self.list[largest]
                    self.list[largest] = temp
                    self.heapify(largest)
            except IndexError:
                return
    
    def __eq__(self, other):
        """ == Checks if two matrices are equal."""
        return self.list == other.list and self.type == other.type

    def __ne__(self, other):
        """!= Check if two matrices are not equal."""
        return not self.__eq__(other)

h = Heap(0)
h.append(1)
h.append(4)
h.append(6)
h.append(1)
h.append(4)
h.append(3)
h.append(3)
print h
h.heapify(0)
print h
l = [1,2,3,4,5]
for i in range(len(l)/2, -1, -1):
    print i
l = buildheap([1, 2, 3, 4, 5, 6, 7], 0)
print l
