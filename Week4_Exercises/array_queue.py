# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#from ..exceptions import Empty


class Empty(Exception):
  pass


class ArrayQueue:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY  # Note we use a list to implement Array
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)   # Circular Array  ---Wei Pang
    self._size -= 1
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self.data))     # double the array size
    avail = (self._front + self._size) % len(self._data)   # Circular Array again ---Wei Pang
    self._data[avail] = e
    self._size += 1

  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    walk = self._front
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[walk]            # intentionally shift indices
      walk = (1 + walk) % len(old)         # use old size as modulus
    self._front = 0                        # front has been realigned


if __name__ == '__main__':
  Q= ArrayQueue()
                        # return value    first<-- Q <--Last
  Q.enqueue(5)          # –                 [5]
  Q.enqueue(3)          # –                 [5, 3]
  a=len(Q)           # 2                 [5, 3]
  a=Q.dequeue( )          # 5                 [3]
  a=Q.is_empty( )         # False             [3]
  a=Q.dequeue( )          # 3                 [ ]
  a=Q.is_empty( )         # True              [ ]
 # Q.dequeue( )          # “error”           [ ]
  a=Q.enqueue(7)          # –                 [7]
  a=Q.enqueue(9)          # –                 [7, 9]
  a=Q.first()             # 7                 [7, 9]
  a=Q.enqueue(4)          # –                 [7, 9, 4]
  a = Q.__len__()  # 3                 [7, 9, 4]
  a=Q.dequeue( )          # 7                  [9, 4]