class Animal(object):
    #inherits from object
    def __init__(self):
        #This function is required for classes, and it's used to initialize the objects it creates.
        # __init__() always takes at least one argument, self, that refers to the object being created
        #self can be not written in the arguments
        pass


class Animals(object):#裡面要是object不能是隨意的參數
    #let class be an object
    #self refer to object itself
    #object has attribute: name

    """Makes cute animals."""
    is_alive = True
    def __init__(self, name):
        self.name = name
    pass

zebra = Animals("Jeffrey")
print zebra.name

class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    #上面是member variables 儲存在每個 class object

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart("Nancy")
my_cart.add_item("juice", 23)

print "*************  Inheritance  *************"

#Inheritance is the process by which one class takes on the attributes and methods of another
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

# class that inherits from Customer
# class new_class(derived class):
class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
# we don't define the display_cart method in the body of ReturningCustomer,
# but it will still have access to that method via inheritance
monty_python.display_cart()
monty_python.display_order_history()

print "*************  override  *************"
# one class that inherits from another to not only take on the methods and attributes of its parent,
# but to override one or more of them.
class Employee(object):
    """Models real-life employees!"""
    #Each class needs to have __init__
    #每個function都需要使用 (self)
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee(Employee):
    #Override function in Employee
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

"""
class Derived(Base):
   def m(self):
       return super(Derived, self).m()
"""


class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

#inherited from Employee

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

#我們希望使用跟在Employee class中有相同名稱的function "calculate_wage"
#但是希望是用到在PartTimeEmployee class中的這個function
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Nancy") #指定新物件為class
print milton.full_time_wage(23)


class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
        # 當值不管是在class中創立，還是在建立新物件時傳遞進入，呼叫class member variables都一樣

    def drive_car(self):
        self.condition = "used"
        #在class中宣告的也是在self底下的memeber variables

    def __repr__(self):
        return "(%s, %s, %s)" % (self.model, self.color, str(self.mpg))
    # __repr__() 用於print out東西，當return 一個值就是告訴python 如何print out object


my_car = Car("DeLorean", "silver", 88)