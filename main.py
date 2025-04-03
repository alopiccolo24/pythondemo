from LinkedList import LinkedList
import sys

def client_management_system():

    clients = LinkedList()

    def add_client():
        try:
            name = input("Provide the client's name: ")
            phone = input("Provide the client's phone number: ")
            birth = input("Provide the client's date of birth: ")
            client_data = f"{name}, {phone}, {birth}"
            clients.append(client_data)
            print("You've added a new client")
        except Exception as e:
            print(f"Error adding client: {e}

    def display_client():
        if clients.is_empty():
            print("No clients in the system")
            return

        print("Current Clients:")
        current = clients.head
        while current:
            name, phone, birth = current.data.split(", ")
            print(f"Name: {name}, Phone: {phone}, Date of Birth: {birth}")
            current = current.next

    def search_client():
        search_name = input("Enter the client's name: ")
        current = clients.head
        found = False
        while current:
            name, phone, birth = current.data.split(", ")
            if name == search_name:
                print(f"Client found: Name: {name}, Phone: {phone}, Date of Birth: {birth}")
                found = True
                break
            current = current.next
        if not found:
            print("Client not found")

    def delete_client():
        delete_name = input("Enter name to delete: ")
        current = clients.head
        prev = None

        while current:
            name, phone, birth = current.data.split(", ")
            if name == delete_name:
                if prev:
                    prev.next = current.next
                else:
                    clients.head = current.next
                print("Client deleted")
                return
            prev = current
            current = current.next
        print("Client not found")

    while True:
        print("\nType the number for the action you wish to perform and then hit Enter")
        print("1. Add a new client")
        print("2. Display a list of all current clients")
        print("3. Search for a client")
        print("4. Delete a client")
        print("5. Quit")

        choice = input("What do you want to do? ")

        if choice == "1":
            add_client()
        elif choice == "2":
            display_client()
        elif choice == "3":
            search_client()
        elif choice == "4":
            delete_client()
        elif choice == "5":
            sys.exit()
        else:
            print("I'm sorry, this is not an allowed action")

if __name__ == "__main__":
    client_management_system()
        


