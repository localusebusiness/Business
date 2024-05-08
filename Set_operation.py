class SetOperation:
    def __init__(self, initialcount):
        self._s = []
        for _ in range(initialcount):
            e = input("Enter the number in set: ")
            self.add(e)

    def get_set(self):
        return self._s

    def add(self, e):
        if e not in self._s:
            self._s.append(e)

    def remove(self, e):
        if e in self.get_set():
            self.get_set().remove(e)

    def __str__(self):
        string = "\n{ "
        for i in range(len(self.get_set())):
            string += str(self.get_set()[i]) + ","
        string += "}\n"
        return string

    def __contains__(self, e):
        return e in self._s

    def intersection(self, setB):
        newSet = SetOperation(0)
        for i in range(len(self.get_set())):
            for j in range(len(setB.get_set())):
                if self.get_set()[i] == setB.get_set()[j]:
                    newSet.add(self.get_set()[i])
        return newSet

    def union(self, setB):
        newSet = self
        for e in setB.get_set():
            if e not in self.get_set():
                newSet.add(e)
        return newSet

    def difference(self, setB):
        newSet = SetOperation(0)
        for e in self.get_set():
            if e not in setB.get_set():
                newSet.add(e)
        return newSet

    def isSubsetOf(self, setB):
        for e in setB.get_set():
            if e not in self.get_set():
                return False
        return True


s1 = SetOperation(int(input("Enter total number of elements in set s1: ")))
print(str(s1))

s2 = SetOperation(int(input("Enter total number of elements in set s2: ")))
print(str(s2))

choice = 0
while choice != 7:
    print("|-------------------|")
    print("| Menu              |")
    print("| 1.Remove          |")
    print("| 2.Contains        |")
    print("| 3.Intersection    |")
    print("| 4.Union           |")
    print("| 5.Difference      |")
    print("| 6.Subset          |")
    print("| 7.Exit            |")
    print("|-------------------|")

    choice = int(input("Enter Choice: "))
    if choice == 1:
        e = input("Enter the element to remove from set 1: ")
        s1.remove(e)
        print(str(s1))
        print(str(s2))
    elif choice == 2:
        e = input("Enter the element to search in set s2: ")
        if e in s2:
            print("Number Present in Set")
        else:
            print("Number is not Present in Set")
        print(str(s1))
        print(str(s2))
    elif choice == 3:
        s3 = s1.intersection(s2)
        print(str(s1))
        print(str(s2))
        print(str(s3))
    elif choice == 4:
        s3 = s1.union(s2)
        print(str(s1))
        print(str(s2))
        print(str(s3))
    elif choice == 5:
        s3 = s1.difference(s2)
        print(str(s1))
        print(str(s2))
        print(str(s3))
    elif choice == 6:
        print("Create a Set B for checking Subset or not")
        issubset = s1.isSubsetOf(s2)
        print("Set A = " + str(s1))
        print("Set B = " + str(s2))
        if issubset:
            print("Set B is the Subset of Set A")
        else:
            print("Set B is not a Subset of Set A")
