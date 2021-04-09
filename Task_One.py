# класс Node для определения элемента списка
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# Создаем линейный односвзяный список
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    # Добавление элементов в конец списка
    def add(self, x):
        self.length += 1
        if self.first == None:
            # self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
        else:
            # здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)

    # Вывод содержимого списка
    def __str__(self):
        if self.first != None:
            current = self.first
            out = str(current.value) + '   '
            while current.next != None:
                current = current.next
                out += str(current.value) + '   '
            return out
        return 'LinkedList '

    # Метод удаления дупликатов
    def RemoveDuplicates(self):
        new_list = LinkedList()
        new = self.__str__().split('   ')
        for item in new:
            if item not in new_list.__str__():
                new_list.add(item)
        return new_list

    def len(self):
        length = 0
        if self.first != None:
            current = self.first
            while current.next != None:
                current = current.next
                length += 1
        return length + 1  # +1 для учета self.first

    def GetSum(self):
        length = 0
        current = None
        key = self.len()
        if self.first != None:
            current = self.first
            while current.next.value != self.last.value:
                current = current.next
                length += 1
            if key == length:
                current = current.value
        sum = self.last.value + current.value
        return sum



