#!/usr/bin/env python3
#
#       Author:    Wei Pang
#       E-mail:    pangweijlu@gmail.com
#       Website:
#
#       File Name: C6_16.py
#       Description:
#           change the implementation of arraystack, this file is based on the following author:
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
#       Last Modified:
#           2017-12-15



from array_stack import ArrayStack
import unittest


class Full(Exception):
    pass


class MyStack(ArrayStack):
    def __init__(self, maxlen=None):
        super().__init__()
        self._maxlen = maxlen

    def push(self, e):
        """Add element e to the top of the stack."""
        if self._maxlen != None:
            if self.__len__() >= self._maxlen:

                raise Full("Stack is full!!!")

        self._data.append(e)




if __name__ == '__main__':

    S = MyStack(5)
    for i in range(5):
        try:
            S.push(i)
        except Exception as e:
            print(e)

    S.push(2)

