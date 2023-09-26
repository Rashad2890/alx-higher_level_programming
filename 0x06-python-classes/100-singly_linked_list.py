""" module that creates and prints a linked list in python """


class Node(object):
    """ init the data and set defaults, create nodes in linked list

    Args:
        object: the object.
    """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node) is True:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList(object):
    """ a singly linked list

        Args:
            object: the object or instance of a class we are given
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if not self.__head:  # no head, return the new head object
            self.__head = Node(value, self.__head)
            return None
        if value < self.__head.data:  # if new data is less, it is new head
            self.__head = Node(value, self.__head)
            return None
        new_node = self.__head
        while new_node.next_node and new_node.next_node.data < value:
            """ while there is a next node and that data is less, next """
            new_node = new_node.next_node
        new_node.next_node = Node(value, new_node.next_node)

    def __repr__(self):
        """ reprint itself, repr for developers str for consumers """
        if not self.__head:
            return ""
        temp = self.__head
        string = ""
        while temp is not None:
            try:
                string += str(temp.data)
                temp = temp.next_node
                string += "\n"
            except:
                pass
        return string[:-1]

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.__head = new_node

    def size(self):
        current = self.__head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.__head
        found = False
        while current and found is False:
            if current.get_data() is data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self):
        current = self.__head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
