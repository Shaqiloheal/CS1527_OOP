# the queue implemented by Python list
#
# Author: Wei Pang
# Based on the original implementation from http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaQueueinPython.html
# which is from the book "Problem Solving with Algorithms and Data Structures using Python" By Brad Miller and David Ranum, Luther College
#
# As mentioned in the above link,
#
# "We need to decide which end of the list to use
# as the rear and which to use as the front. The implementation shown in
# Listing 1 assumes that the rear is at position 0 in
# the list. This allows us to use the insert function on
# lists to add new elements to the rear of the queue.
# The pop operation can be used to remove the front
# element (the last element of the list). Recall that this
# also means that enqueue will be O(n) and dequeue will be O(1)."
#
#
# Note we could also assume the rear is at the end of the list, as suggested
# in the Goodrich book Chapter 6.2.2:
#  enqueue by using list.append(e), and dequeue by using pop(0)


class Empty(Exception):
  pass

class ListQueue:
    def __init__(self):
        self.items = []

    def __len__(self):
        """Return the number of elements in the queue, added by Wei Pang"""
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self.items.pop()

    def size(self):
        return len(self.items)

    def first(self):
        """ Add by Wei Pang
        Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self.items[len(self.items)-1]


if __name__ == '__main__':
  Q= ListQueue()
                        # return value    first<-- Q <--Last
  Q.enqueue(5)          # –                 [5]
  Q.enqueue(3)          # –                 [5, 3]
  a=Q.__len__()           # 2                 [5, 3]
  a=Q.dequeue( )          # 5                 [3]
  a=Q.is_empty( )         # False             [3]
  a=Q.dequeue( )          # 3                 [ ]
  a=Q.is_empty( )         # True              [ ]
 # Q.dequeue( )          # “error”           [ ]
  a=Q.enqueue(7)          # –                 [7]
  a=Q.enqueue(9)          # –                 [7, 9]
  a=Q.first()             # 7                 [7, 9]
  a=Q.enqueue(4)          # –                 [7, 9, 4]
  a = Q.__len__()         # 3                 [7, 9, 4]
  a=Q.dequeue()          # 7                  [9, 4]
  a=Q.dequeue()          # 9                  [4]

