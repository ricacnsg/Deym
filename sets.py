import os
import platform
import time

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
    print(("-" * 31) +
          "\n|Choose type of Union:        |\n" +
          ("-" * 31) +
          "\n|1.) Display union of all sets|" +
          "\n|2.) Pick sets to Union)      |\n" +
          ("-" * 31) )
    choice = input("Enter choice: ")
    if choice == "1":
        union_all()
        clear_choice = input("Do you want to clear screen? [y/n] ").lower().strip()
        if clear_choice == "y":
            clear_screen()
    elif choice == "2":
        print("\nAvailable sets:")
        for name, items in universal_set.items():
            print(f"{name}: {', '.join(items) if items else 'Empty'}")
        
        selected_sets = []
        print("\nEnter the name of the sets to union (Press Ctrl+D to finish):")
        try:
            while True:
                set_name = input("Set name: ").strip()
                
                if set_name not in universal_set:
                    print(f"Set '{set_name}' does not exist. Please enter a valid set name.\n")
                    continue
                
                if set_name in selected_sets:
                    print(f"Set '{set_name}' is already in the union list.")
                else:
                    selected_sets.append(set_name)
        except EOFError:
            print("")
    
        select_union(selected_sets)
        clear_choice = input("\nDo you want to clear screen? [y/n] ").lower().strip()
        if clear_choice == "y":
            clear_screen()
        elif clear_choice == "n":
            pass
        else:
            print("Invalid option.\n")
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
        print(f"\nU(Union) of all sets: {{{', '.join(union_of_all)}}}")
        print()

def select_union(selected_sets):
    if not selected_sets:
        print("No sets selected for union.")
        return
    
    union_of_selected_sets = set()
    for set_name in selected_sets:
        union_of_selected_sets.update(set(universal_set[set_name]))
    
    print(f"\nUnion of selected sets ({', '.join(selected_sets)}): {{{', '.join(union_of_selected_sets)}}}")

# Intersection Set Functionality
def intersection_set(selected_sets):
    if not universal_set:
        print("No sets available to perform intersection.")
        return

    intersection_result = set(universal_set[selected_sets[0]])

    for set_name in selected_sets[1:]:
        intersection_result &= set(universal_set[set_name])

    formatted_result = ', '.join(str(item) for item in intersection_result)
    print(f"\nIntersection of selected sets ({', '.join(selected_sets)}): {{{formatted_result}}}")

# Disjoint Set Functionality (hindi pa final)
def disjoint_set(selected_sets):
    if len(selected_sets) < 2:
                        print("You need to select at least two sets.")
                        return

    result = True
    for i in range(len(selected_sets)):
        for j in range(i+1, len(selected_sets)):
            set1 = set(universal_set[selected_sets[i]])
            set2 = set(universal_set[selected_sets[j]])
            if set1 & set2: 
                result = False
                break
        if not result:
            break

    if result:
        print("\n\nThe selected sets are disjoint.")
    else:
        print("\n\nThe selected sets are not disjoint (they have common elements).\n")

def difference(set1, set2):
    if set1 and set2 not in universal_set:
        print(f"\n{set1} and {set2} is not found in universal set\n")
        return
    else:
        difference_result = set(universal_set[set1]) - set(universal_set[set2])
        print(f"\nThe difference of set '{set1}' - set '{set2}' is: {difference_result}\n")
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


def complement_set(set_name):
    if not universal_set:
        print("The universal set is empty. Cannot perform complement operation.")
        return

    universal_elements = {item for subset in universal_set.values() for item in subset}
    set_elements = set(universal_set[set_name])
    complement_result = universal_elements - set_elements

    formatted_result = ', '.join(str(item) for item in complement_result)
    print(f"\nThe complement of set '{set_name}' is: {{{formatted_result}}}\n")


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
                print("\nAvailable sets for intersection: ")
                display_all_sets(universal_set)
                selected_sets = []
                while True:
                    try:
                        set_choice = input("\nEnter the name of the set to intersect (Press Ctrl+D to finish): ", end = "").strip().capitalize()

                        if set_choice not in universal_set:
                            print(f"Set '{set_choice}' does not exist.")
                            continue

                        if set_choice not in selected_sets:
                            selected_sets.append(set_choice)
                        else:
                            print(f"Set '{set_choice}' already selected.")
                    except ValueError:
                        print("Invalid input! Please enter a valid set name.")
                    except EOFError:
                        break

                if len(selected_sets) < 2:
                    print("At least two sets are required for intersection.")
                    return
                intersection_set(selected_sets)
            elif operation_choice == 3:
                print("\nAvailable sets for complement operation:")
                display_all_sets(universal_set)
                set_name = input("\nEnter the name of the set to find its complement: ").strip().capitalize()
                if set_name not in universal_set:
                    print(f"Set '{set_name}' does not exist.")
                    return
                else:
                    complement_set(set_name)
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
                print("\nAvailable sets for disjoint check: ")
                display_all_sets(universal_set)

                selected_sets = []
                while True:
                    try:
                        set_choice = input("Enter a set name to include in the disjoint check (Press Ctrl+D to finish): ").strip().capitalize()
                        if set_choice not in universal_set:
                            print(f"Set '{set_choice}' does not exist.")
                            continue

                        if set_choice not in selected_sets:
                            selected_sets.append(set_choice)
                        else:
                            print(f"Set '{set_choice}' is already in the list.")
                    except ValueError:
                        print("\nInvalid input! Please enter a valid set name.")
                    except EOFError:
                        break

                disjoint_set(selected_sets)
                clear_choice = input("Do you want to clear screen? [y/n] ").lower().strip()
                if clear_choice == "y":
                    clear_screen()
                elif clear_choice == "n":
                    pass
            elif operation_choice == 7:
                print("Exiting Operations...")
                clear_screen()
                break
            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input! Please enter a valid number for your choice.")

main()