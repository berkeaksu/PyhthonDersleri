class ParentClass():
    def send_message(self):
        print("Bu alan içerisinde mesaj verilecektir.")


class BaseClass(ParentClass):
    def send_message(self):
        print("BaseClass üzerinden gelen mesaj")
        
parent = ParentClass()
parent.send_message()

base = BaseClass()
base.send_message()