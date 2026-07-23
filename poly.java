class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None


class Poly:
    def __init__(self):
        self.head = None

    def insert(self, co, po):
        new_node = Node(co, po)

        if self.head is None or self.head.power < po:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        while current.next and current.next.power > po:
            current = current.next

        if current.next and current.next.power == po:
            current.next.coeff += co
        elif current.power == po:
            current.coeff += co
        else:
            new_node.next = current.next
            current.next = new_node


def add_poly(poly1, poly2):
    p1 = poly1.head
    p2 = poly2.head

    result = Poly()

    while p1 and p2:
        if p1.power == p2.power:
            result.insert(p1.coeff + p2.coeff, p1.power)
            p1 = p1.next
            p2 = p2.next
        elif p1.power > p2.power:
            result.insert(p1.coeff, p1.power)
            p1 = p1.next
        else:
            result.insert(p2.coeff, p2.power)
            p2 = p2.next

    while p1:
        result.insert(p1.coeff, p1.power)
        p1 = p1.next

    while p2:
        result.insert(p2.coeff, p2.power)
        p2 = p2.next

    return result


def display(poly):
    current = poly.head
    terms = []

    while current:
        terms.append(f"{current.coeff}x^{current.power}")
        current = current.next

    print(" + ".join(terms))


# Interactive Mode
poly1 = Poly()
poly2 = Poly()

n1 = int(input("Enter number of terms in Polynomial 1: "))
for i in range(n1):
    coeff = int(input("Enter coefficient: "))
    power = int(input("Enter power: "))
    poly1.insert(coeff, power)

n2 = int(input("\nEnter number of terms in Polynomial 2: "))
for i in range(n2):
    coeff = int(input("Enter coefficient: "))
    power = int(input("Enter power: "))
    poly2.insert(coeff, power)

print("\nPolynomial 1:")
display(poly1)

print("Polynomial 2:")
display(poly2)

result = add_poly(poly1, poly2)

print("Resultant Polynomial:")
display(result)