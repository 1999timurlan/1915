class Grandfather1:
    def __init__(self):
        super().__init__()
        self.eyes= "green"
class Grandmother1:
    def __init__(self):
        super().__init__()
        self.height= 175
class Grandfather2:
    def __init__(self):
        super().__init__()
        self.hair= "curly"
class Grandmother2:
    def __init__(self):
        super().__init__()
        self.skin= "white"

class Father(Grandfather1,Grandmother1):
    def __init__(self):
        super().__init__()
        print(f"Father have {self.eyes} eyes")
        print(f"Father have {self.height} height")
        print()
class Mother(Grandfather2,Grandmother2):
    def __init__(self):
        super().__init__()
        print(f"Mother have {self.hair} hair")
        print(f"Mother have {self.skin} skin")
        print()

class Child(Father,Mother):
    def print_info(self):
        print(f"Child have {self.eyes} eyes")
        print(f"Child have {self.height} height")
        print(f"Child have {self.hair} hair")
        print(f"Child have {self.skin} skin")
        print()


Denus=Child()
Denus.print_info()




