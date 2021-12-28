class Car(object):

    def _init_(self, model, color, speed, company, speed_limit):  
        self.color=color
        self.model=model
        self.speed=speed
        self.company=company
        self.speed_limit-speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarated")
        "accelarated functionality"

    def change_gear(self, gear_type):
        print("gear_changed")
        "gear functionality"

audi=Car("a6", "filled blue", "120km", "audi" "200km")
print(audi.start())
