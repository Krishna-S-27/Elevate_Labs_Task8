import random

def show_main_menu():
    print("\nMain Menu:")
    print("1. Product Information")
    print("2. Order Support")
    print("3. Technical Support")
    print("4. Speak to a Human Agent")
    print("5. Exit")

def product_info():
    print("\nProduct Information Menu:")
    print("1. View product categories")
    print("2. Pricing details")
    print("3. Return to Main Menu")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("ChatBot: We offer Electronics, Clothing, and Home Appliances.")
    elif choice == "2":
        print("ChatBot: Prices vary by product. Visit our website for the latest deals.")
    elif choice == "3":
        return
    else:
        print("ChatBot: Invalid choice. Please try again.")

def order_support():
    print("\nOrder Support Menu:")
    print("1. Track my order")
    print("2. Cancel my order")
    print("3. Return to Main Menu")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        order_id = input("Please enter your Order ID: ").strip()
        print(f"ChatBot: Tracking Order {order_id}... Estimated delivery: 3 days.")
    elif choice == "2":
        order_id = input("Please enter your Order ID: ").strip()
        print(f"ChatBot: Order {order_id} has been cancelled successfully.")
    elif choice == "3":
        return
    else:
        print("ChatBot: Invalid choice. Please try again.")

def tech_support():
    print("\nTechnical Support Menu:")
    print("1. Troubleshoot device")
    print("2. Request technician visit")
    print("3. Return to Main Menu")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("ChatBot: Please restart your device and check if the issue persists.")
    elif choice == "2":
        print("ChatBot: Technician will visit within 48 hours.")
    elif choice == "3":
        return
    else:
        print("ChatBot: Invalid choice. Please try again.")

print("ChatBot: Welcome to High-End Menu-Driven Rule-Based Chatbot!")
user_name = input("May I have your name? ").strip().title()
print(f"Hello {user_name}! How can I assist you today?")

while True:
    show_main_menu()
    option = input("Choose an option: ").strip()

    if option == "1":
        product_info()
    elif option == "2":
        order_support()
    elif option == "3":
        tech_support()
    elif option == "4":
        responses = [
            "Connecting you to a live agent... Please wait..",
            "One moment, transferring you to a human representative...",
            "Please hold while I connect you to an available agent..."
        ]
        print("ChatBot:", random.choice(responses))
    elif option == "5":
        print(f"ChatBot: Thank you for contacting SmartSupport, {user_name}. Goodbye! ")
        break
    else:
        print("ChatBot: Invalid choice. Please select from the menu.")
