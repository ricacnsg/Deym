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
                print("CREATE A SET\n--------------")
                set_name = input("Enter name for set: ").strip().capitalize()

                if set_name in universal_set:
                    print(f"\n{set_name} is already existing!")
                    load_and_clear()
                    continue

                create_set(set_name)
                clear_screen()
                print(f"Successfully added {set_name}!")
                display_all_sets(universal_set)
                load_and_clear()
            elif choice == 2:
                display_all_sets(universal_set)
                try:
                    set_name = input("\nEnter a set to put elements in: ").capitalize().strip()
                    load_and_clear()
                    if set_name not in universal_set:
                        print("Set is not existing. Please create set first.")
                        continue

                    print("INSERT ELEMENTS\n" + "-" * 18 + "\nPress 'Ctrl' + 'D' to end inserting elements.\n")
                    while True:
                        try:
                            elements = input("Enter an element: ").strip()
                            if not elements:
                                break
                            add_elements(set_name, elements)
                        except EOFError:
                            break
                except Exception:
                    print("Invalid input. Redirecting to Main Interface")
                    load_and_clear()
                    continue
                print("\n")
                clear_screen()
            elif choice == 3:
                display_all_sets(universal_set)
                try:
                    set_name = input("\nEnter a set to remove elements from: ").capitalize().strip()
                    load_and_clear()
                    if set_name not in universal_set:
                        print(f"Set '{set_name}' does not exist. Redirecting to Main\n")
                        load_and_clear()
                        continue

                    if not universal_set:
                        print("There are no elements to delete. Redirecting to Main Interface.")
                        load_and_clear()
                        continue
        
                    else:
                        print("DELETE ELEMENTS" + "\n" + ("-" * 15) + "\n")
                        print(f"\nCurrent Set '{set_name}':")
                        print("-" * 30)
                        print(f"{'Index':<10}{'Element':<20}")
                        print("-" * 30)
                        for i, el in enumerate(universal_set[set_name], start = 1):
                            print(f"{i:<10}{el:<20}")
                        print("-" * 30)
                        
                        if not universal_set[set_name]:
                            print(f"\nThere are no elements to delete. {set_name} is an Empty Set. Redirecting to Main Interface.")
                            load_and_clear()
                            continue

                        print("Press 'Ctrl+D' when done.\n")
                        while True:
                            try:
                                index = input("Enter the index of the element to remove: ").strip()
                                print(delete_elements(set_name, index))
                                if not universal_set[set_name]:
                                    print(f"\nThere are no elements to delete. {(universal_set[set_name])} is an Empty Set.")
                                    load_and_clear()
                                    break
                            except EOFError: 
                                clear_screen()
                                break 
                except Exception:
                    print("\nInvalid input. Redirecting to Main Interface.")
                    load_and_clear()
                    continue
            elif choice == 4:
                if not universal_set:
                    print("There are no sets to delete. Redirecting to Main Interface.")
                    load_and_clear()
                    return

                print("DELETE SET" + "\n" + ("-" * 10))
                display_all_sets(universal_set)
                print("-" * 31)
                try:
                    set_name = input("Enter set name to be deleted: ").strip().capitalize()
                    delete_set(set_name)
                    if set_name not in universal_set:
                        print(f"{set_name} not existing. Redirecting to Main Interface.")
                        load_and_clear()
                        continue
                    print(f"\n{set_name} deleted successfully! ")
                    load_and_clear()
                except Exception:
                    print("\nInvalid input. Redirecting to Main Interface.")
                    load_and_clear()
                    continue
            elif choice == 5:
                display_all_sets(universal_set)
                clear_choice = input("\nDo you want to clear screen? [y/n]").lower().strip()
                if clear_choice == "y":
                    load_and_clear()
                else:
                    continue
                print()
            elif choice == 6:
                print("DISPLAY SETS" + "\n" + ("-" * 12) + "\n")
                perform_operations()
            elif choice == 7:
                print("Exiting App")
                clear_screen()
                break
            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Please enter a valid numeric choice.")
            clear_screen()

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
    print("\nDisplaying Sets and Elements:")
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
        index -= 1
        removed_element = universal_set[set_name].pop(index)
        return f"Element '{removed_element}' removed from the set '{set_name}'."
    except ValueError:
        return "Index must be a valid integer."
    except IndexError:
        return f"Invalid index. The set '{set_name}' is now an empty set."

#{len(universal_set[set_name])}

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
          "\n|2.) Pick sets to Union       |\n" +
          ("-" * 31) )
    choice = input("Enter choice: ")
    load_and_clear()
    if choice == "1":
        union_all()
    elif choice == "2":
        print("\nAvailable Sets:")
        for name, items in universal_set.items():
            print(f"{name}: {', '.join(items) if items else 'Empty'}")
        
        selected_sets = []
        print("\n" + ("-" * 22) + "\nPress Ctrl+D to finish\n")
        try:
            while True:
                set_name = input("Set Name to perform Union operation: ").strip()
                
                if not set_name:
                    print("\nUnion process stopped.")
                    return

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
    else:
        print("Invalid option.")
    return

def union_all():
    if not universal_set:
        print("Universal set is empty.\n")
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
    
    print(f"\nUnion of selected sets {{{', '.join(selected_sets)}}}: {{{', '.join(union_of_selected_sets)}}}")


def intersection_set(selected_sets):
    if not selected_sets:
        print("\nNo sets selected for intersection.")
        return

    if len(selected_sets) < 2:
        print("\nAt least two sets are required for intersection.")
        return
    
    intersection_result = set(universal_set[selected_sets[0]])

    for set_name in selected_sets[1:]:
        if set_name in universal_set:
            intersection_result &= set(universal_set[set_name])
        else:
            print(f"Set '{set_name}' does not exist. Skipping this set.")
            continue

    if len(intersection_result) == 0:
        print("No common elements found in the selected sets.")
    else:
        formatted_result = ', '.join(str(item) for item in intersection_result)
        print(f"\nIntersection of selected sets ({', '.join(selected_sets)}): {{{formatted_result}}}")


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

def difference(set_names):
    invalid_sets = [s for s in set_names if s not in universal_set]
    if invalid_sets:
        print(f"\nThe following sets were not found in the universal set: {', '.join(invalid_sets)}\n")
        return

    diff_result = set(universal_set[set_names[0]])
    for s in set_names[1:]:
        diff_result = diff_result.difference(set(universal_set[s]))

    print(f"\nThe difference of sets {' - '.join(set_names)} is: {diff_result}\n")
    return diff_result

def symmetric_difference(sets):
    if not sets:
        print("\nThe provided list of sets is empty. Please provide valid sets.\n")
        return
    
    if sets not in universal_set:
        print(f"\nThe following sets were not found in the universal set." )
        return

    all_sets = [set(universal_set[s]) for s in sets]

    symmetric_diff_result = all_sets[0]
    for s in all_sets[1:]:
        symmetric_diff_result = symmetric_diff_result.symmetric_difference(s)

    print(f"\nThe symmetric difference among the sets {', '.join(sets)} is: {symmetric_diff_result}\n")
    return symmetric_diff_result



def complement_set(set_name):
    if not universal_set:
        print("The universal set is empty. Cannot perform complement operation.")
        return

    universal_elements = {item for subset in universal_set.values() for item in subset}
    set_elements = set(universal_set[set_name])
    complement_result = universal_elements - set_elements

    formatted_result = ', '.join(str(item) for item in complement_result)
    print(f"\nThe complement of set '{set_name}' is: {{{formatted_result}}}")


def check_if_empty(set_name):
    if set_name not in universal_set:
        return f"\nSet '{set_name}' does not exist in the universal set."
    elif not universal_set[set_name]:
        return f"\nThe set '{set_name}' is empty."
    else:
        elements = ', '.join(universal_set[set_name])
        return f"\nThe set '{set_name}' is not empty and contains: {elements}"


def loading():
    start_time = time.time() 

    while time.time() - start_time < 1:
        print(".", end="", flush=True)
        time.sleep(.33) 
    
    print()

def load_and_clear():
    print("\nLoading", end = "")
    loading()
    clear_screen()

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
            print("|7. Check if Set is Empty    |")
            print("|8. Exit Operations          |")
            print("-" * 30)

            operation_choice = int(input("Enter choice: "))
            clear_screen()

            if operation_choice == 1:
                print("UNION\n" +
                      "-" * 5 + "\n")
                union_choice()
                clear_choice = input("\nDo you want to clear screen? [y/n]").lower().strip()
                if clear_choice == "y":
                    load_and_clear()
                else:
                    continue
            elif operation_choice == 2:
                print("\nINTERSECTION\n" +
                      "-" * 12 + "\n")
                print("\nAvailable sets for intersection: ")
                display_all_sets(universal_set)
                selected_sets = []
                print("\n" + ("-" * 22) + "\nPress 'Ctrl+D' when done.\n")
                while True:
                    try:
                        set_choice = input("Enter the name of the set to intersect: ").strip().capitalize()

                        if set_choice not in universal_set:
                            print(f"Set '{set_choice}' does not exist.")
                            continue

                        if set_choice not in selected_sets:
                            selected_sets.append(set_choice)
                        else:
                            print(f"Set '{set_choice}' already selected.")
                    except EOFError:
                        break 

                if len(selected_sets) < 2:
                    print("At least two sets are required for intersection.")
                    return

                intersection_set(selected_sets)
                clear_choice = input("\nDo you want to clear screen? [y/n]").lower().strip()
                if clear_choice == "y":
                    load_and_clear()
                else:
                    continue
            elif operation_choice == 3:
                print("\nCOMPLEMENT\n" +
                      "-" * 10 + "\n")
                print("\nAvailable sets for complement operation:")
                display_all_sets(universal_set)
                set_name = input("\nEnter the name of the set to find its complement: ").strip().capitalize()
                if set_name not in universal_set:
                    print(f"Set '{set_name}' does not exist.")
                    return
                else:
                    complement_set(set_name)
                clear_choice = input("\nDo you want to clear screen? [y/n]").lower().strip()
                if clear_choice == "y":
                    load_and_clear()
                else:
                    continue
            elif operation_choice == 4:
                print("\nDIFFERENCE\n" +
                      "-" * 10)
                display_all_sets(universal_set)
                print("\n" + ("-" * 22) + "\nPress 'Ctrl+D' when done.\n")
                set_names = []
                while True:
                    try:
                        set_name = input("Enter set name to perform Difference Operation: ").strip().capitalize()
                        set_names.append(set_name)
                    except EOFError:
                        break
                if len(set_names) < 2:
                    print("\nAt least two sets are required for the difference operation.\n")
                else:
                    difference(set_names)
                clear_choice = input("\nDo you want to clear screen? [y/n]").lower().strip()
                if clear_choice == "y":
                    load_and_clear()
                else:
                    continue
            elif operation_choice == 5:
                    print("\nSYMMETRIC DIFFERENCE\n" +
                      "-" * 20 + "\n")
                    display_all_sets(universal_set)
                    print("\n" + ("-" * 22) + "\nPress 'Ctrl+D' when done.\n")
                    sets = []
                    while True:
                        try:
                            set_name = input("Enter set name for Symmetric Difference Operation: ").strip().capitalize()
                            sets.append(set_name)
                        except EOFError:
                            print("\nInput stopped.")
                            break

                    if len(sets) < 2:
                        print("\nAt least two sets are required for the symmetric difference operation.\n")
                    else:
                        print()
                        symmetric_difference(sets)
                    clear_choice = input("\nDo you want to clear screen? [y/n]").lower().strip()
                    if clear_choice == "y":
                        load_and_clear()
                    else:
                        continue
            elif operation_choice == 6:
                print("\nDISJOINT\n" +
                      "-" * 8 + "\n")
                print("\nAvailable sets for disjoint check: ")
                display_all_sets(universal_set)

                selected_sets = []
                print("\n" + ("-" * 22) + "\nPress 'Ctrl+D' when done.\n")
                while True:
                    try:
                        set_choice = input("Enter a set name to include in the disjoint check: ").strip().capitalize()
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
                clear_choice = input("\nDo you want to clear screen? [y/n]").lower().strip()
                if clear_choice == "y":
                    load_and_clear()
                else:
                    continue
            elif operation_choice == 7:
                print("\nCHECK IF A SET IS EMPTY\n" +
                      "-" * 23 + "\n")
                display_all_sets(universal_set)
                set_name = input("\nEnter the name of the set to check: ").strip().capitalize()
                result = check_if_empty(set_name)
                print(result)
                if clear_choice == "y":
                    load_and_clear()
                else:
                    continue
            elif operation_choice == 8:
                print("Exiting Operations...")
                clear_screen()
                break
            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input! Please enter a valid number for your choice.")

main()