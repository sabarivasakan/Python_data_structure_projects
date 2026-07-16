class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    # Add at end
    def append(self, name):
        new = Node(name)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    # Add at beginning
    def prepend(self, name):
        new = Node(name)
        new.next = self.head
        self.head = new

    # Insert at position
    def insert(self, name, position):
        new = Node(name)

        if position == 0:
            new.next = self.head
            self.head = new
            return

        temp = self.head
        count = 0

        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            return

        new.next = temp.next
        temp.next = new

    # Delete by song name
    def delete(self, name):
        if self.head is None:
            return

        if self.head.name == name:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next.name == name:
                temp.next = temp.next.next
                return
            temp = temp.next

    # Display playlist
    def show(self):
        temp = self.head
        while temp:
            print(temp.name, end=" -> ")
            temp = temp.next
        print("None")




playlist = Playlist()

playlist.append("Believer")
playlist.append("Shape of You")
playlist.prepend("Perfect")
playlist.insert("Faded", 2)

print("Playlist:")
playlist.show()

playlist.delete("Shape of You")

print("\nAfter Deletion:")
playlist.show()