from replit import clear

welcome_txt = "Welcome to my fibonacci program"
print(welcome_txt.center(100, "-"))


def main():

    try:
        number = int(input("Please enter a number so that I can show you the Fibonacci sequence for that number: "))
    except ValueError:
        error_txt = "Please type number."
        print("||| " + error_txt + " |||")
        return main()

    fib_list = []
    a, b = 1, 1
    while len(fib_list) < number:
        fib_list.append(a)
        a, b = b, a + b

    fib_txt = f"Fibonacci pattern: {fib_list}"
    length_txt = len(fib_txt) + 4
    print("+" + "-" * (length_txt - 2) + "+")
    print("| " + fib_txt + " |")
    print("+" + "-" * (length_txt - 2) + "+")

    start_again = input("Do you want to try again: Type 'Yes' or 'No': ").lower()
    if start_again == "yes":
        clear()
        return main()
    elif start_again == "no":
        print("Please wait...")
        print("Thanks.")
        print("I hope you have a good time.")

if __name__ == '__main__':
    main()