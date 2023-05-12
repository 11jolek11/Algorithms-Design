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

    if start is None:
        return new_node

    ptr = start

    while (ptr.next is not None):
        ptr = ptr.next
    ptr.next = new_node
    return start


# Function two Multiply two polynomial Numbers
def multiply(poly1, poly2, poly3):
    ptr1 = poly1
    ptr2 = poly2

    while (ptr1 is not None):
        while (ptr2 is not None):

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
    print(str(poly3))
    # print(str(remove_duplicates(poly3)))
