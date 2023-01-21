

class Vehicle:
    def __init__(self,license):
        self.license = license

    def purpose(self):
        print("generic vehicle")


class Car(Vehicle):

    def __init__(self,license,wheels):
        Vehicle.__init__(self,license)
        self.wheels = wheels

    def purpose(self):
        print("specific vehicle: Car")


    def update_wheels(self,num_wheels):
        try:
            print("attempting to update wheels")
            10/num_wheels
            self.wheels = num_wheels
        except Exception as e:
            print(type(e))
        finally:
            print("in finally")



c = Car("L1234",4)
c.purpose()
c.update_wheels(0)