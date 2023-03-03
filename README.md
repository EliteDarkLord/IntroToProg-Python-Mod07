# Assignment 07 - Pickling and Exception Handling
**Dev:** *KPhan*  
**Date:** *2/28/2023*

## Introduction
In this assignment, I will explain the steps I used to create a simple python calculator script that will enable a user to select a menu choice, two inputs to calculate, and what calculation to perform. The script will also “pickle” the user’s option into a binary file as to encrypt the user’s menu choice. The script was created in Pycharm IDE and will be run on the Pycharm IDE and OS Command/Terminal on a Macintosh operating system.

## Objective
My objective for this script is to provide the user a menu of options numbered 1-6. As shown in code block below. The options I’ve provided are the following:
1)	Calculate Sum
2)	Calculate Difference
3)	Calculate Product
4)	Calculate Quotient
5)	Exit Program

![Python Calculator Menu](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure1.png)  
*Figure 1: Python Calculator Menu*

## Drafting the Code

### Defining Variables
The global variables I've defined in this script are represented in *figure 2*

Choice - This global string variable will store the user’s menu choice  
Value1 - This global variable represents the user’s num1 input  
Value2 - This global variable represents the user’s num2 input   
listData - This list variable will store the user’s menu choice into a list object  
strFileName - This file will store the user’s menu choice in binary form

![Defining Global Variables](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure2.png)  
*Figure 2: Defining global variables*

### Classes
The python calculator script is organized into five classes as shown in *figure 3*
**IO** – Responsible for inputs and outputs of various functions  
**Processor** – performs the math operations/calculations and error handling  
**Num1_invalid** – Error handling for user’s first num input  
**Num2_invalid** – error handling for user’s second num input  
**Divide_by_zero** – error handling to check for dividing by 0 particularly for calculating quotient.

![Python Calculator Classes](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure3.png)  
*Figure 3: Python Calculator Classes*

### IO (Input/Output)
The main purpose of Class IO is to gather the user’s input of two numbers and output the results based on the user’s choice. I created the following functions under this class as shown in *figure 4*:

![Class IO Functions](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure4.png)  
*Figure 4: Class IO Functions*

### Menu()
This function is  a simple display of the python calculator menu that provides the user information to choose from.

![Menu of Options](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure5.png)
*Figure 5: Menu of Options*

### User_Input_task()
This function uses the *input()* function to request user input by prompting a message to make a menu selection. In line 45, the user’s input choice is stored in an object list and is saved into a file. Line 50 returns the user’s choice to be utilized elsewhere within the script as shown in *figure 6*.

![Storing user's menu choice](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure6.png)
*Figure 6: Storing user's menu choice*

### output_sum(), output_difference(), output_product(), output_quotient()
The next set of functions shown in *figure 7* in this class are the outputs of the sum, difference, product, and quotient. The summary for all of these functions is defining a local variable to another class function value and outputs a message with the results of the calculation. Each function passes two arguments or parameters which is “num1” and “num2”. These parameters represents the user’s two input values for each calculation to perform.

![Output functions for sum, difference, product, quotient](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure7.png)
*Figure 7: Output functions for sum, difference, product, and quotient*

### addvalues(num1, num2)
In *figure 8* this function under class “Processor” is utilized when the user selects option ‘1’ from the menu to calculate the sum of two values. The function passes two parameters “num1” and “num2” and will add the two values. I used while loop with  a nested Try, Except to capture any invalid inputs such as a char for either input one or two. In the try code block, the script will request for two number inputs from the user and converts the value into a float. An if-elif-else statement is inside this Try block to capture any invalid data by the user. From lines 94-98 if the user’s first input is a char then the script will raise the exception function num1_invalid and num2_invalid for num2. If the user inputs two valid inputs, then the script will execute the else condition and add the two inputs and break the while loop. After the loop is broken, the function returns the sum of the two values.

The same code structure is similar for functions subtractvalues() and multiplyvalues().

![add values function](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure8.png)
*Figure 8: add values function*

### dividevalues(num1, num2)
Shown in *figure 9* dividevalues passes two arguments which contains the user’s two inputs to calculate the quotient. Similar to the addvalues coding structure, this function uses a while loop to continuously check the user’s inputs. However, in the if-elif-else statement, if the user inputs 0 or 0.0 as the second value, a custom divide_by_zero exception class will be raised as shown in figure 10 and outputs a custom error message to the user shown in *figure 11*.

![divide values function](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure9.png)
*Figure 9: dividevalues function*

![divide_by_zero exception class](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure10.png)
*Figure 10: divide_by_zero exception class*

![Divide by 0 custom message output](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure11.png)
*Figure 11: Divide by 0 custom message output*

The last function shown in *figure 12*  inside the processor class is the save_data_to_file. The purpose of this function was to dump the user’s menu choice input into a file in binary format. This function passes the global variable file name and data list, opens the file and with the imported pickle in line 10 of the script, the dump() pickle function is used to place the list of data or user’s choice into the file in binary format.

![Pickling](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure12.png)
*Figure 12: Pickling Function*

### Exception  Handling
In *figure 13* there are three Exception classes in this script as mentioned earlier. Num1_invalid and num2_invalid  will be raised if the user enters a char or symbol for the first or second number input. This exception will prompt a message indicating the entered input is not valid.

![Custom message for exception handling](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure13.png)
*Figure 13: Custom message for exception handling*

### Presentation
In *figure 14*, the last section of this script contains the presentation of the user’s choices. In this while loop in line 215, the menu is displayed followed by the definition of global variable ‘choice’ assigned to the returned value of IO.user_input_task(). Based on this function, the variable ‘choice’ will be compared in the if-elif-else statements and execute the functions within. The script will run the script until the user enters ‘5’ to exit the program.

![Presentation](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure14.png)
*Figure 14: Presentation*

## Running the Code
### Pycharm IDE
*Figure 15* shows a snapshot of performing option 1 of the python calculator to calculate the sum of two values. I entered the char ‘a’ to raise the custom class exception num1_invalid with the custom message.

![Pycharm IDE Output](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure15.png)
*Figure 15: Pycharm IDE output of Calculate Sum*

Similarly I tested the divide_by_zero class exception to capture the exception handling as shown in *figure 16*.

![output of divide_by_zero exception](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure%2016.png)
*Figure 16: Raising divide_by_zero exception*

### OS Command/Terminal
*Figure 17* provides an example of the python calculator script on OS Command/Terminal. Using the terminal command cd to change directory to the appropriate folder containing the program file. Then using ls to list out the files within the designated folder I performed the quotient calculation to raise the divide_by_zero exception. 

*Figure 18* provides a snapshot of the pickling function storing the user’s choice into a file in binary format.

![Python Calculator on OS Command/Terminal](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure17.png)
*Figure 17: Python Calculator on OS Command/Terminal*

![User's choice in binary format](https://github.com/EliteDarkLord/IntroToProg-Python-Mod07/blob/main/Github%20pictures/figure18.png)
*Figure 18: User's menu choice in binary format*

## Conclusion
From watching the course video, reading chapter 7 of the textbook, and following along the labs in the “_Mod7PythonProgrammingNotes” document, and watching various videos recommended by the instructor,  I was able to utilize Pycharm IDE to create a working python calculator script with exception handling and pickling.

