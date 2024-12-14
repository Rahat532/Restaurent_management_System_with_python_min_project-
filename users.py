from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address) 
        self.cart=Order()
    def view_menu(self,restaurent):
        restaurent.menu.show_menu()
    def add_to_cart(self,restaurent,item_name,quantity):
        item = restaurent.menu.find_item(item_name)
        #print(f'We Have total {item.quantity} items Available')
        if item is not None:
            if quantity >item.quantity:
                print("Item quantity is too high")
            else:
              item.quantity = quantity
              self.cart.add_item(item)
              print("The Item has been added !!")
        else:
            print("Item not found")
    def view_cart(self):
        print("**View Cart**")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price}")
    def pay_bill(self):
        print(f'Total {self.cart.total_price} payments successful')
        print("Thank you for shopping with us!!")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, phone, email, address, age,designation, salary):
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary
#emp=Employee("Rohim",9342343,"rohim32@gmail.com","Dhaka",25,"managers",234234)
#print(emp.name)
class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)

    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)
    
    def view_menu(self, retaurent):
        retaurent.menu.show_menu()
        
    
    


            