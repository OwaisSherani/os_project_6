#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name)
# that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "Default Bank"  # Class variable
    def __init__(self, acc_holder):
        self.acc_holder = acc_holder  # Public variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Update the class variable
    
    def display_info(self):
        print(f"Account Holder: {self.acc_holder}")
        print(f"Bank Name: {Bank.bank_name}")

#Create instances of the Bank class
acc1 = Bank("Owais")
acc2 = Bank("Huzaifa")

#display initial bank name
acc1.display_info()
acc2.display_info()

#Change the bank name using the class method
Bank.change_bank_name("HBL Bank")


# Show that the change affects all instances
acc1.display_info()
acc2.display_info()