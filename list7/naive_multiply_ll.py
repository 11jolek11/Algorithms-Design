class Node:
    def __init__(self) -> None:
       self.power = None
       self.coeff = None
       self.next = None

    def __str__(self) -> str:
        current_node = self
        repr = f'{current_node.coeff}x^{current_node.power}'
        while current_node.next is not None:
            repr += f' + {current_node.next.coeff}x^{current_node.next.power}'
            current_node = current_node.next
        return repr


def add_node(start, coeff, power):
    new_node = Node()
    new_node.power = power
    new_node.coeff = coeff

    if start == None:
        return new_node

    ptr = start

    while (ptr.next != None):
        ptr = ptr.next
    ptr.next = new_node
    return start


# def remove_duplicates(start):
#     ptr1 = start
#     ptr2 = None
#     duplicate = None

#     while (ptr1 != None and ptr1.next != None):
#         ptr2 = ptr1

#         while (ptr2.next != None):
#             if (ptr1.power == ptr2.next.power):
#                 ptr1.coeff += ptr2.coeff
#                 duplicate = ptr2.next
#                 ptr2.next = ptr2.next.next
#             else:
#                 ptr2 = ptr2.next
#         ptr1 = ptr1.next

# def remove_duplicates(start):
#     ptr = start
#     while ptr.next != None:
#         if ptr.power == ptr.next.power:
#             ptr.coeff += ptr.next.coeff
#             temp = ptr.next
#             ptr.next = ptr.next.next
#         else:
#             ptr = ptr.next
#     return start


# Function two Multiply two polynomial Numbers
def multiply(poly1, poly2, poly3):
    
    # Create two pointer and store the
    # address of 1st and 2nd polynomials
    ptr1 = poly1
    ptr2 = poly2
     
    while (ptr1 != None):
        while (ptr2 != None):
  
            # Multiply the coefficient of both
            # polynomials and store it in coeff
            coeff = ptr1.coeff * ptr2.coeff
  
            # Add the powerer of both polynomials
            # and store it in power
            power = ptr1.power + ptr2.power
  
            # Invoke addnode function to create
            # a newnode by passing three parameters
            poly3 = add_node(poly3, coeff, power)
  
            # move the pointer of 2nd polynomial
            # two get its next term
            ptr2 = ptr2.next
          
        # Move the 2nd pointer to the
        # starting point of 2nd polynomial
        ptr2 = poly2
  
        # move the pointer of 1st polynomial
        ptr1 = ptr1.next
      
    # this function will be invoke to add
    # the coefficient of the elements
    # having same powerer from the resultant linked list
    # print("########")
    # print(str(poly3))
    # print("########")
    # remove_duplicates(poly3)
    return poly3


def multiply_from_list(a, b):
    poly1 = None
    poly2 = None

    # for i in range(len(a), -1, -1):
    #     poly1 = add_node(poly1, a[i], i)

    # for i in range(len(b), -1, -1):
    #     poly2 = add_node(poly2, b[i], i)


    for i in range(len(a)):
            poly1 = add_node(poly1, a[i], len(a) - 1 - i)
    # print(str(poly1))

    for i in range(len(b)):
        poly2 = add_node(poly2, b[i], len(b) - 1 - i)
    # print(str(poly2))

    return multiply(poly1, poly2, None)

# Driver Code
if __name__=='__main__':
    poly1 = None
    poly2 = None
    poly3 = None
  
    # Creation of 1st Polynomial: 3x^2 + 5x^1 + 6
    poly1 = add_node(poly1, 3, 3)
    poly1 = add_node(poly1, 6, 1)
    poly1 = add_node(poly1, -9, 0)
  
    # Creation of 2nd polynomial: 6x^1 + 8
    poly2 = add_node(poly2, 9, 3)
    poly2 = add_node(poly2, -8, 2)
    poly2 = add_node(poly2, 7, 1)
    poly2 = add_node(poly2, 2, 0)
  
    # Displaying 1st polynomial
    print("1st Polynomial:- ", end = '')
    # print(str(poly1))
  
    # Displaying 2nd polynomial
    print("2nd Polynomial:- ", end = '')
    # print(str(poly2))
    # calling multiply function
    poly3 = multiply(poly1, poly2, poly3)
  
    # Displaying Resultant Polynomial
    print("Resultant Polynomial:- ", end = '')
    # print(str(poly3))
    # print(str(remove_duplicates(poly3)))
    multiply_from_list([3, 2], [3, 2, 1])
