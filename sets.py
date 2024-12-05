import os
import platform
universal_set = {}

def main():
    print("      TO DO APPLICATION")
    while True:
        try:
            print("-" * 30)
            print("|Options:                    |")
            print("------------------------------")
            print("|1. Create a Set             |")
            print("|2. Add Elements to Set      |")
            print("|3. Remove Elements to Set   |")
            print("|4. Delete Set               |")
            print("|5. Display All Sets         |")
            print("|6. Perform Operations       |")
            print("|7. Exit App                 |")
            print("-" * 30)

            choice = int(input("Enter choice: "))
            clear_screen()

            if choice == 1:
                set_name = input("\nEnter name for set: ").strip().capitalize()
                create_set(set_name)
                display_all_sets(universal_set)
            elif choice == 2:
                display_all_sets(universal_set)
                set_name = input("\nEnter a set to put elements in: ").capitalize().strip()
                print("Type 'ctrl' + 'd' to end inserting elements.")
                while True:
                    try:
                        elements = input("Enter a element: ").strip()
                        add_elements(set_name, elements)
                    except EOFError:
                        break
            elif choice == 3:
                display_all_sets(universal_set)
                set_name = input("\nEnter a set to remove elements from: ").capitalize().strip()
                if set_name not in universal_set:
                    print(f"Set '{set_name}' does not exist.")
                else:
                    print(f"Set '{set_name}' elements: {universal_set[set_name]}")
                    while True:
                        try:
                            index = input("Enter the index of the element to remove (or type 'done' to stop): ").strip()
                            if index.lower() == 'done':
                                break
                            print(delete_elements(set_name, index))
                        except EOFError:
                            break
            elif choice == 4:
                display_all_sets(universal_set)
                category = input("Enter set name to be deleted: ").strip().capitalize()
                delete_set(set_name)
            elif choice == 5:
                display_all_sets(universal_set)
            elif choice == 6:
                perform_operations()
            elif choice == 7:
                print("Exiting App")
                clear_screen()
                break
            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Please enter a valid numeric choice.")

def create_set(set_name):
    if set_name in universal_set:
        return f"The set '{set_name}' already exists in the universal set."
    
    universal_set[set_name] = []
    return f"Set '{set_name}' added successfully!"

def add_elements(set_name, elements):
    if set_name not in universal_set:
        return f"Set '{set_name}' does not exist in the universal set."

    universal_set[set_name].append(elements)
    return f"Elements {elements} added to the set '{set_name}'."

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def display_all_sets(universal_set):
    print("\nCurrent sets and their elements:")
    if not universal_set:
        print("No sets available.")
    else:
        for name, set_items in universal_set.items():
            print(f"{name}: {', '.join(set_items) if set_items else 'Empty'}")

def delete_elements(set_name, index):
    if set_name not in universal_set:
        return f"Set '{set_name}' does not exist in the universal set."
    
    try:
        index = int(index) 
        removed_element = universal_set[set_name].pop(index)
        return f"Element '{removed_element}' removed from the set '{set_name}'."
    except ValueError:
        return "Index must be a valid integer."
    except IndexError:
        return f"Invalid index. The set '{set_name}' has {len(universal_set[set_name])} elements."

def delete_set(set_name):
    if set_name in universal_set:
        del universal_set[set_name]
        print(f"Set '{set_name}' deleted successfully.")
    else:
        print(f"Set '{set_name}' does not exist!")
main()