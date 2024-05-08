class hashTable:
    # initialize hash Table
    def __init__(self):

        self.size = int(input("Enter the Size of the hash table : "))
        # initialize table with all elements 0
        self.table = list(None for i in range(self.size))
        self.elementCount = 0
        self.comparisons = 0

    # method that checks if the hash table is full or not
    def isFull(self):
        if self.elementCount == self.size:
            return True

        return False

    # method that returns position for a given element
    def hashFunction(self, element):
        return element % self.size

    # method that inserts element into the hash table
    def insert(self, record):
        # checking if the table is full
        if self.isFull():
            print("Hash Table Full")

        else:
            self.comparisons = 0
            position = self.hashFunction(record)

            # checking if the position is empty
            if self.table[position] is None:
                self.table[position] = record
                self.elementCount += 1
                self.comparisons += 1

            # collision occured hence we do linear probing
            else:
                print("Collision has occured , finding new Position.")
                self.comparisons += 1
                while self.table[position] is not None:
                    position = (position + 1) % self.size
                    if position >= self.size:
                        position = 0
                    self.comparisons += 1

                self.table[position] = record
                self.elementCount += 1
            print(f"Number of comparisons for inserting {record}: {self.comparisons}")

    def search(self, record):
        found = False
        position = self.hashFunction(record)
        self.comparisons = 0

        initial_position = position  # Keep track of the initial position for cyclic checking
        self.comparisons += 1

        while self.table[position] is not None:
            if self.table[position] == record:
                found = True
                print(
                    f"Record found at position {position} and total comparisons are {self.comparisons}"
                )
                return position

            position += 1
            if position >= self.size:
                position = 0

            if position == initial_position:
                # If we have cycled through the entire table and reached the initial position again, break the loop
                break

            self.comparisons += 1

        if not found:
            print("Record not found", self.size)
            return False

    def remove(self, record):
        position = self.search(record)
        if position is not False:
            self.table[position] = None
            print("Element" + str(record) + " removed successfully")
            self.elementCount -= 1
        else:
            print("Element" + str(record) + " not found")

    # method to display the hash table
    def display(self):
        print("\n")
        for i in range(self.size):
            print(str(i) + "\t\t" + str(self.table[i]))
        # print("The number of phonebook records in the Table are : " + str(self.elementCount))


h1 = hashTable()

choice = 0
while choice != 8:
    print("|-------------------|")
    print("| Menu              |")
    print("| 1.Insert         |")
    print("| 2.Display         |")
    print("| 3.Search         |")
    print("| 4.Remove         |")
    print("| 5.Exit           |")

    ch = int(input("Enter your choice"))
    if ch == 1:
        key = int(input("Enter the key"))
        h1.insert(key)
    elif ch == 2:
        h1.display()

    elif ch == 3:
        key = int(input("Enter the element to Search"))
        h1.search(key)

    elif ch == 4:
        key = int(input("Enter the element to Search"))
        h1.remove(key)