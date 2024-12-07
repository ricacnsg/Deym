import os
import platform

universal_set = {}

def main():
    print("      DEYM'S SET OPERATION")
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
                        elements = input("Enter an element: ").strip()
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

# Intersection Set Functionality
def intersection_set():
    if not universal_set:
        print("No sets available to perform intersection.")
        return

    print("\nAvailable sets for intersection: ")
    display_all_sets(universal_set)

    selected_sets = []
    while True:
        try:
            set_choice = input("\nEnter the name of the set to intersect (or 'done' to finish): ").strip().capitalize()

            if set_choice.lower() == 'done':
                break
            elif set_choice not in universal_set:
                print(f"Set '{set_choice}' does not exist.")
                continue

            if set_choice not in selected_sets:
                selected_sets.append(set_choice)
                print(f"Set '{set_choice}' added for intersection.")
            else:
                print(f"Set '{set_choice}' already selected.")
        except ValueError:
            print("Invalid input! Please enter a valid set name.")

    if len(selected_sets) < 2:
        print("At least two sets are required for intersection.")
        return

    # Perform intersection
    intersection_result = set(universal_set[selected_sets[0]])
    for set_name in selected_sets[1:]:
        intersection_result &= set(universal_set[set_name])

    print(f"Intersection of selected sets ({', '.join(selected_sets)}): {intersection_result}")
    print()

# Disjoint Set Functionality (hindi pa final)
def disjoint_set():
    if len(universal_set) < 2:
        print("At least two sets are required for this operation.")
        return

    print("\nAvailable sets for disjoint check: ")
    display_all_sets(universal_set)

    selected_sets = []
    while True:
        try:
            set_choice = input("Enter a set name to include in the disjoint check (or type 'done' to finish): ").strip().capitalize()
            if set_choice.lower() == 'done':
                break
            elif set_choice not in universal_set:
                print(f"Set '{set_choice}' does not exist.")
                continue

            selected_sets.append(set_choice)
        except ValueError:
            print("Invalid input! Please enter a valid set name.")

    if len(selected_sets) < 2:
        print("You need to select at least two sets.")
        return

    # Check for disjoint sets
    result = True
    for i in range(len(selected_sets)):
        for j in range(i+1, len(selected_sets)):
            set1 = set(universal_set[selected_sets[i]])
            set2 = set(universal_set[selected_sets[j]])
            if set1 & set2:  # If the intersection is not empty, they are not disjoint
                result = False
                break
        if not result:
            break

    if result:
        print("The selected sets are disjoint.")
    else:
        print("The selected sets are not disjoint (they have common elements).")

def difference(set1, set2):
    if set1 and set2 not in universal_set:
        print(f"{set1} and {set2} is not found in universal set")
        return
    else:
        difference_result = set(universal_set[set1]) - set(universal_set[set2])
        print(f"The difference of set '{set1}' - set '{set2}' is: {difference_result}")
        return difference_result

def symmetric_difference(sets):
    if not sets:
        print("The provided list of sets is empty. Please provide valid sets.")
        return

    all_sets = [set(universal_set[s]) for s in sets if s in universal_set]
    if len(all_sets) < len(sets):
        print("One or more provided sets do not exist in the universal set.")
        return

    symmetric_diff_result = all_sets[0]  

    for s in all_sets[1:]:
        symmetric_diff_result = symmetric_diff_result.symmetric_difference(s)

    print(f"The symmetric difference among the sets {', '.join(sets)} is: {symmetric_diff_result}")
    return symmetric_diff_result


def complement_set():
    if not universal_set:
        print("The universal set is empty. Cannot perform complement operation.")
        return

    print("\nAvailable sets for complement operation:")
    display_all_sets(universal_set)

    set_name = input("\nEnter the name of the set to find its complement: ").strip().capitalize()
    if set_name not in universal_set:
        print(f"Set '{set_name}' does not exist.")
        return

    # Calculate the complement
    universal_elements = {item for subset in universal_set.values() for item in subset}
    set_elements = set(universal_set[set_name])
    complement_result = universal_elements - set_elements

    print(f"The complement of set '{set_name}' is: {complement_result}")


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
                display_all_sets(universal_set)
                set1 = input("Enter set 1: ")
                set2 = input("Enter set 2: ")
                difference(set1, set2)
            elif operation_choice == 5:
                display_all_sets(universal_set)
                sets = input("Enter the names of the sets (comma-separated): ").strip().split(',')
                sets = [s.strip().capitalize() for s in sets]
                symmetric_difference(sets)
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
