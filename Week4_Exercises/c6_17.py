
#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: C6_16.py
#       Description:
#           change the implementation of arraystack
#
#       Last Modified:
#           2014-07-04 12:46:09
#
#     2017-12-12  Modified by Wei Pang pangweijlu@gmail.com
#
#
#

from array_stack import ArrayStack


class Full(Exception):
  pass


class MyStack1(ArrayStack):
    def __init__(self, maxlen=None):
        self._maxlen = maxlen
        self._data = [] if maxlen is None else [None] * maxlen

    def push(self, e):
        """Add element e to the top of the stack."""
        if self._maxlen != None:
            if self.__len__() >= self._maxlen:

                raise Full("Stack is full!!!")

        self._data.append(e)

if __name__ == '__main__':
    S = MyStack1(5)
    S.pop()
    S.push(2)
