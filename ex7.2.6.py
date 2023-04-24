def print_list(products):
    print("Product list:")
    for product in products:
        print(product)

def print_count(products):
    print("Number of products:", len(products))

def print_contains(products, name):
    if name in products:
        print(name, "is on the list")
    else:
        print(name, "is not on the list")

def print_frequency(products, name):
    count = products.count(name)
    print(name, "appears", count, "time(s)")

def remove_product(products, name):
    if name in products:
        products.remove(name)
        print(name, "removed from the list")
    else:
        print(name, "not found in the list")

def add_product(products, name):
    products.append(name)
    print(name, "added to the list")

def print_invalid(products):
    invalid_products = [p for p in products if len(p) < 3 or not p.isalpha()]
    if invalid_products:
        print("Invalid products:")
        for product in invalid_products:
            print(product)
    else:
        print("No invalid products")

def remove_duplicates(products):
    unique_products = list(set(products))
    products.clear()
    products.extend(unique_products)
    print("Duplicates removed")

def main():
    products = input("Enter a list of products, separated by commas: ").lower().split(",")

    while True:
        print()
        print("Please select an option:")
        print("1. Print the list of products")
        print("2. Print the number of products")
        print("3. Check if a product is on the list")
        print("4. Check the frequency of a product")
        print("5. Remove a product from the list")
        print("6. Add a product to the list")
        print("7. Print invalid products")
        print("8. Remove duplicates")
        print("9. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print_list(products)
        elif choice == 2:
            print_count(products)
        elif choice == 3:
            name = input("Enter a product name: ")
            print_contains(products, name)
        elif choice == 4:
            name = input("Enter a product name: ")
            print_frequency(products, name)
        elif choice == 5:
            name = input("Enter a product name: ")
            remove_product(products, name)
        elif choice == 6:
            name = input("Enter a product name: ")
            add_product(products, name)
        elif choice == 7:
            print_invalid(products)
        elif choice == 8:
            remove_duplicates(products)
        elif choice == 9:
            break
        else:
            print("Invalid choice")

    print("Goodbye!")

if __name__ == "__main__":
    main()
