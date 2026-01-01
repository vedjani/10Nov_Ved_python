print("*****Welcome*****")

orders=[]
order_id = 1
def add_order():
    global order_id

    name=(input("Enter customer name: "))
    device=(input("Enter device name: "))
    issue=(input("Enter issue date: "))
    due=(input("Enter due date: "))

    order={
        "order_id":order_id,
        "name": name,
        "device":device,
        "issue":issue,
        "due":due
        
    }
    orders.append(orders)
    print("order added")
    print("order id :",order_id)
    order_id = order_id + 1 
    return order


def generate_bill():
    ord_id=(input("Enter order id: "))
    for i in orders:
        if i[orders[order_id]] == ord_id:
            parts_cost = int(input("Enter parts cost: "))
            repair_fee = int(input("Enter repair fee: "))

            subtotal = parts_cost + repair_fee
            tax = subtotal * 0.18
            total = subtotal + tax

            print("\n========= BILL =========")
            print("Order ID      :",order["order_id"])
            print("Customer Name :",order["name"])
            print("Device Type   :",order["device"])
            print("Issue         :",order["issue"])
            print("Due Date      :",order["due"])
            print("------------------------")
            print("Parts Cost    :", parts_cost)
            print("Repair Fee    :", repair_fee)
            print("Tax (18%)     :", tax)
            print("Total Amount  :", total)
            print("========================\n")

            break
        else:
            print("Order Id not found")

while True:
    print("=== FixTrack Menu ===")
    print("1. Add Repair Order")
    print("2. Generate Bill")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_order()
    elif choice == "2":
        generate_bill()
    elif choice == "3":
        print("Thank you for using FixTrack")
        break
    else:
        print("Invalid choice\n")