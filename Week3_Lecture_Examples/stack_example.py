from arraystack import ArrayStack

# sample usage
if __name__ == '__main__':
    
    # mystack = ArrayStack()
    # mystack.push(5) # [5]
    # mystack.push(3) # [5, 3]
    # print(len(mystack)) # 2
    # mystack.pop()   # [5]
    # print(mystack.is_empty()) # False
    # mystack.pop()   # []
    # print(mystack.is_empty()) # True
    # #mystack.pop()    # "error"
    # mystack.push(7) # [7]
    # mystack.push(9) # [7, 9]
    # print(mystack.top())  # 9
    # mystack.push(4) # [7, 9, 4]
    # print(len(mystack)) # 3
    # mystack.pop()   # [7, 9]
    # mystack.push(6) # [7, 9, 6]
    # mystack.push(8) # [7, 9, 6, 8]
    # mystack.pop()   # [7, 9, 6]
    # print(mystack._data) # prints the stack
    
    mystack = ArrayStack()
    print(mystack.is_empty())
    mystack.push('hello')
    mystack.push(7)
    print(mystack.__len__())
    print(mystack.pop())