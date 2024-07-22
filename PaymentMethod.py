# PaymentMethod.py
# please add "from PaymentMethod import PaymentMethod" to main.py

class PaymentMethod:
    def __init__(self):
        self.payment_type = None

    def select_payment_method(self):
        while True:
            print("Select a payment method:")
            print("1. Credit Card")
            print("2. Cash")
            choice = input("Enter the payment method (1/2): ")

            if choice == "1":
                self.payment_type = "Credit Card"
                break
            elif choice == "2":
                self.payment_type = "Cash"
                break
            else:
                print("Invalid choice. Please enter 1 for Credit Card or 2 for Cash.")

    def process_payment(self, amount):
        if self.payment_type == "Credit Card":
            credit_card_number = input("Enter your credit card number: ")
            # You can add further validation and processing for credit card payments here.
            print(f"Payment of ${amount:.2f} successfully processed with Credit Card ending in {credit_card_number[-4:]}.")
        elif self.payment_type == "Cash":
            print(f"Please pay ${amount:.2f} in cash at the payment counter.")
        else:
            print("No payment method selected. Please select a payment method first.")
