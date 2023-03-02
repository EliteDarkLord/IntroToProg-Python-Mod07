# ------------------------------------------------- #
# Title: Assignment07
# Description: This is a simple python calculator. User will have options from a menu
#              When chosen a menu, two inputs will be prompted and calculated. If user enters
#              invalid data, an exception will prompt to the user.
# ChangeLog: (Who, When, What)
# KPhan,<02.22.2023>,Created Script
# ------------------------------------------------- #

import pickle  # imports code from another code file

# Data -------------------------------------------- #
choice = ""  # contains user's menu choice
value1 = 0  # represents user's first num input
value2 = 0  # represents user's second num input
listData = []  # stores user's choice into a list object
strFileName = 'AppData.dat'  # file that will contain user's choice


# This class contains the input and output for the script
class IO:

    @staticmethod
    def menu():
        print('''
        Python Calculator
        ===Menu===
        1) Calculate Sum
        2) Calculate Difference
        3) Calculate Product
        4) Calculate Quotient
        5) Exit Program
        ''')
        print()

    @staticmethod
    def user_input_task():
        """
        returns the user's choice from the menu

        :return: (string) user's option input
        """

        choice = input("Please enter an option to perform: ")
        list = [choice]

        # Pickling user's menu choice
        Processor.save_data_to_file(strFileName, list)

        return choice

    # Output the sum of two values
    @staticmethod
    def output_sum():
        sum = Processor.addvalues(num1=value1, num2=value2)
        print("\nThe sum of the two values is: ", sum)

    # Output the difference of two values
    @staticmethod
    def output_difference():
        difference = Processor.subtractvalues(num1=value1, num2=value2)
        print("\nThe difference of the two values is: ", difference)

    # Output the product of two values
    @staticmethod
    def output_product():
        product = Processor.multiplyvalues(num1=value1, num2=value2)
        print("\nThe product of the two values is: ", product)

    # Output the quotient of two values
    @staticmethod
    def output_quotient():
        quotient = Processor.dividevalues(num1=value1, num2=value2)
        print("\nThe quotient of the two values is: ", quotient)


# This class will process the user's input data to perform the calculations
class Processor:

    # Calculate the sum of two values
    def addvalues(num1, num2):
        """
        returns the sum of two floats

        :param num1: (float) first user's num input
        :param num2: (float) user's second number input
        :return: (float) sum of num1 and num2
        """
        while True:
            try:
                num1 = input("Please enter the 1st number: ")
                num2 = input("Please enter the 2nd number: ")

                if str(num1).isalpha():
                    raise num1_invalid.__str__(num1)

                elif str(num2).isalpha():
                    raise num2_invalid.__str__(num2)

                else:
                    sum = float(num1) + float(num2)
                    break

            except Exception as e:
                print("A char was entered as input. Expected int or float\n")

        return sum

    # Calculate the difference of two values
    def subtractvalues(num1, num2):

        while True:

            try:
                num1 = input("\nPlease enter the 1st number: ")
                num2 = input("Please enter the 2nd number: ")

                if str(num1).isalpha():
                    raise num1_invalid.__str__(num1)

                elif str(num2).isalpha():
                    raise num2_invalid.__str__(num2)

                else:
                    difference = float(num1) - float(num2)
                    break

            except Exception as e:
                print("A char was entered as input. Expected int or float\n")

        return difference

    # Calculate the product of two values
    def multiplyvalues(num1, num2):

        while True:

            try:
                num1 = input("\nPlease enter the 1st number: ")
                num2 = input("Please enter the 2nd number: ")

                if str(num1).isalpha():
                    raise num1_invalid.__str__(num1)

                elif str(num2).isalpha():
                    raise num2_invalid.__str__(num2)

                else:
                    product = float(num1) * float(num2)
                    break

            except Exception as e:
                print(e)

        return product

    # Calculate the quotient of two values
    def dividevalues(num1, num2):

        while True:

            try:
                num1 = input("\nPlease enter the 1st number (numerator): ")
                num2 = input("Please enter the 2nd number (denominator): ")

                if str(num1).isalpha():
                    raise num1_invalid.__str__(num1)

                elif str(num2).isalpha():
                    raise num2_invalid.__str__(num2)

                elif int(num2) == 0:
                    raise divide_by_zero()

                else:
                    quotient = float(num1) / float(num2)
                    break

            except Exception as e:
                print(e)

        return quotient

    # Saving user's input into a file
    def save_data_to_file(file_name, list_of_data):
        """

        :param list_of_data: (list) stores list of data
        :param file_name: (string) file name containing list of data
        :return:
        """
        file = open(file_name, "ab")
        pickle.dump(list_of_data, file)

# This class checks if user's first num1 input is valid
class num1_invalid(Exception):
    def __str__(num1):
        print("\nPlease do not use", "(" + num1 + ")", "as an input!")


# This class checks if user's second num2 input is valid
class num2_invalid(Exception):
    def __str__(num2):
        print("\nPlease do not use", "(" + num2 + ")", "as an input!")


# This class checks if function dividevalues contains a 0 for num2
class divide_by_zero(Exception):
    def __str__(self):
        return 'CANNOT DIVIDE BY 0!'


# Presentation ------------------------------------ #
while True:
    IO.menu()
    choice = IO.user_input_task()

    # Option 1: Calculate Sum of two numbers
    if choice == "1":
        IO.output_sum()
        continue

    # Option 2: Calculate Difference of two numbers
    elif choice == "2":
        IO.output_difference()
        continue

    # Option 3: Calculate Product of two numbers
    elif choice == "3":
        IO.output_product()
        continue

    # Option 4: Calculate Quotient of two numbers
    elif choice == "4":
        IO.output_quotient()
        continue

    # Option 6: Exit's program
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print(choice, "is not on the menu!")
        continue
