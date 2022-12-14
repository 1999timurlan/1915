import time
import random
class Cat:
    def __init__(self):
        self.hungry = 50
        self.want_to_toilet = "No"
        self.sleep = 50
        self.holiday = 50

    def eat(self):
        Cat1.hungry+=50

    def go_to_toilet(self):
        Cat1.want_to_toilet = "No"

    def sleeping(self):
        Cat1.sleep+=70
        if Cat1.sleep>100:
            zalishok2=Cat1.sleep-100
            Cat1.sleep-=zalishok2

    def enjoy(self):
        Cat1.holiday+=30
        if Cat1.holiday>100:
            zalishok3=Cat1.holiday-100
            Cat1.holiday-=zalishok3


    def printer(self):
        print(f"Cats hungry={self.hungry}")
        print(f"Cat want sleep={self.sleep}")
        print(f"Cat want to toilet={self.want_to_toilet}")
        print(f"Cats funny={self.holiday}")

    def hungring(self):
        Cat1.hungry-=10


    def toilet(self):
        rand=random.randint(1,5)
        if rand==1:
            Cat1.want_to_toilet = "Yes"

    def get_tired(self):
        Cat1.sleep-=5


    def boring(self):
        Toilet=Cat1.want_to_toilet
        Cat1.holiday-=10
        if Toilet=="Yes":
            Cat1.holiday-=10

Cat1=Cat()


class Food:
    def __init__(self,brand_list):
        self.brand=random.choice(list(brand_list))
        self.nutrition=brand_list[self.brand]["nutrition"]
        self.tasty=brand_list[self.brand]["tasty"]
        self.benefit=brand_list[self.brand]["benefit"]
brand_of_foog={
    "Club 4 paws":{"nutrition":50,"tasty":5,"benefit":10},
    "Brid": {"nutrition": 70, "tasty": 7, "benefit":8},
    "ProPlan": {"nutrition": 30, "tasty": 12, "benefit":24},
}



print("Hello, I am cat")
while True:
    print("----------------------------------------------------------------------")
    Cat1.toilet()
    Cat1.hungring()
    Cat1.boring()
    Cat1.get_tired()
    Cat1.printer()
    print("----------------------------------------------------------------------")
    if Cat1.hungry<1 or Cat1.holiday<1 or Cat1.sleep<1:
        print("Goodbuy!")
        print("You was bad humen!")
        n="    :(    "
        n=n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n
        n=n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n+n
        print(n)
        break
    do=input("What do yuo want to do? (Feed/Play/Sleep/Go to toilet):")

    if do=="Feed":
        Cat.eat(self=Cat1)

    elif do == "Play":
        Cat.enjoy(self=Cat1)

    elif do=="Sleep":
        Cat.sleeping(self=Cat1)


    elif do=="Go to toilet":
        Cat.go_to_toilet(self=Cat1)





















