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

                if set_name not in universal_set:
                    print("Set is not existing. Please create set first.")
                    continue

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
            print(f"{name}: {{{', '.join(set_items) if set_items else ''}}}")

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

def union_choice():
    print("1.) Display union of all sets" +
    "\n2.) Pick sets to Union)")
    choice = input("Enter choice: ")
    if choice == "1":
        union_all()
    elif choice == "2":
        for idx, (name, items) in enumerate(universal_set.items(), 1):
            print(f"{idx}. {name}: {', '.join(items) if items else 'Empty'}")
            selected_sets = []
        while True:
            try:
                set_choice = input("\nEnter the number of the set to union: ").strip()
                set_number = int(set_choice)

                if set_number < 1 or set_number > len(universal_set):
                    print(f"Invalid set number {set_number}. Please choose a valid number.")
                    continue

                selected_set_name = list(universal_set.keys())[set_number - 1]
                
                if selected_set_name not in selected_sets:
                    selected_sets.append(selected_set_name)
                    print(f"Set '{selected_set_name}' added to union list.")
                else:
                    print(f"Set '{selected_set_name}' is already in the union list.")

                print()
            
            except ValueError:
                print("Invalid input. Please enter a valid set number or 'done'.")

            except EOFError:
                break
                    
            select_union(selected_sets)
            print()
    else:
        print("Invalid option.")
    return

def union_all():
    if not universal_set:
        print("Universal set is empty.")
        return
    else:
        union_of_all = set()
        for set_name, set_items in universal_set.items():
            union_of_all.update(set(set_items))
        print(f"U(Union) of all sets: {{{', '.join(union_of_all)}}}")
        print()
    

def select_union(selected_sets):
    if not selected_sets:
        print("No sets selected for union.")
        return
    
    union_of_selected_sets = set()
    for set_name in selected_sets:
        union_of_selected_sets.update(set(universal_set[set_name]))
    
    print(f"Union of selected sets ({', '.join(selected_sets)}): {union_of_selected_sets}")

def perform_operations():
    while True: 
        try:
            print("-" * 30)
            print("|Perform Operations:         |")
            print("------------------------------")
            print("|1. Union Set                |")
            print("|2. Intersection Set         |")
            print("|3. Complement Set           |")
            print("|4. Difference Set           |")
            print("|5. Symmetric Difference Set |")
            print("|6. Disjoint Set             |")
            print("|7. Exit Operations          |")
            print("-" * 30)

            operation_choice = int(input("Enter choice: "))
            clear_screen()

            if operation_choice == 1:
                union_choice()
            elif operation_choice == 2:
                intersection_set()
            elif operation_choice == 3:
                complement_set()
            elif operation_choice == 4:
                difference_set()
            elif operation_choice == 5:
                sym_difference()
            elif operation_choice == 6:
                disjoint_set()
            elif operation_choice == 7:
                print("Exiting Operations...")
                clear_screen()
                break
            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input! Please enter a valid number for your choice.")

main()