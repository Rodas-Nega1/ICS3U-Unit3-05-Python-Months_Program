# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Sept 2021
# This program checks a user's integer value


def main():
    # this function checks if an integer is positive, negative, or a zero

    # input
    month_number = int(input("Enter the number of a month (1-12): "))
    print("")

    # process & output
    if month_number == 1:
        print("January.")

    elif month_number == 2:
        print("February.")

    elif month_number == 3:
        print("March.")

    elif month_number == 4:
        print("April.")

    elif month_number == 5:
        print("May.")

    elif month_number == 6:
        print("June.")

    elif month_number == 7:
        print("July.")

    elif month_number == 8:
        print("August.")

    elif month_number == 9:
        print("September.")

    elif month_number == 10:
        print("October.")

    elif month_number == 11:
        print("November.")

    elif month_number == 12:
        print("December.")

    else:
        print("That is not a month.")

    print("\nDone.")


if __name__ == "__main__":
    main()
