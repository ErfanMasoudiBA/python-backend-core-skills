class Device:
    def __init__(self, brand):
        self.brand = brand

    def turn_on(self) -> None:
        print("Device is turning on.")


class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


object_num1 = Phone("Apple", "iphone 15s")
object_num1.turn_on()
print(object_num1.model)
print(object_num1.brand)
