class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items

    def calculate_total_cost(self,discount):
        total_cost = sum(item.price * item.quantity for item in self.items)

        #discount calculation here
        if(discount != 0):
            total_cost = total_cost * discount

        #tax calculation here
        total_cost += total_cost * 0.03
    
        return total_cost

class Inventory:
    def __init__(self):
        self.items = {}

    def update_inventory(self, items, increase=True):
        for item in items:
            if item.name in self.items:
                if increase:
                    self.items[item.name] += item.quantity  # Increase the quantity
                else:
                    self.items[item.name] -= item.quantity  # Decrease the quantity
                    if self.items[item.name] < 0:
                        self.items[item.name] = 0  # Ensure quantity doesn't go negative
            else:
                if increase:
                    self.items[item.name] = item.quantity   # Add new item to inventory if not already present
                else:
                    self.items[item.name] = 0  # If decreasing and item not present, set quantity to 0

    def check_item_availability(self, item):
        if item.name in self.items and self.items[item.name] >= item.quantity:
            return True
        else:
            return False

class EmailService:
    def send_order_confirmation(self, order):
        # Send order confirmation email to customer
        print(f"Order confirmation email sent to {order.customer.email}")



def main():
    # Create dummy instances
    customer = Customer("John Doe", "john@example.com", "123 Main St")
    items = [Item("Laptop", 1000, 1), Item("Mouse", 20, 2)]
    order = Order(customer, items)
    inventory = Inventory()

    # Update inventory with dummy items
    inventory.update_inventory([Item("Laptop", 1000, 6), Item("Mouse", 20, 10)])

    # Check item availability and process order
    if inventory.check_item_availability(items[0]):
        total_cost = order.calculate_total_cost(0)
        print(f"Total order cost: ${total_cost}")
        inventory.update_inventory(items, False)
        print("Updated Inventory:")
        for item_name, quantity in inventory.items.items():
            print(f"{item_name}: {quantity}")
        email_service = EmailService()
        email_service.send_order_confirmation(order)
    else:
        print("Items not available in inventory.")

if __name__ == "__main__":
    main()
