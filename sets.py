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
                display_all_sets()
            elif choice == 2:
                display_all_sets()
                set_name = input("\nEnter a set to put elements in: ").capitalize().strip()
                print("Type 'ctrl' + 'd' to end inserting elements.")
                while True:
                    try:
                        element = input("Enter a element: ").strip()
                        add_elements(set_name, elements)
                    except EOFError:
                        break
            elif choice == 3:
                display_all_sets()
                set_name = input("\nEnter a set to put elements in: ").capitalize().strip()
                print("Type 'ctrl' + 'd' to end inserting elements.")
                while True:
                    try:
                        element = input("Enter a element to be deleted: ").strip()
                        delete_elements(set_name, elements)
                    except EOFError:
                        break
            elif choice == 4:
                display_all_sets()
                category = input("Enter set name to be deleted: ").strip().capitalize()
                delete_set(set_name)
            elif choice == 5:
                display_all_sets()
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

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

main()