 Program Purpose
 ---------------
   
The purpose of this program is to generate a random password based on user preferences. The user can choose which types of characters the password should include, such as lowercase letters, uppercase letters, numbers, and special symbols. The user can also select how many characters of each type will be included.

The program provides a graphical user interface (GUI) built using Tkinter so users can easily choose their options and generate a password.

Problem the Project Solves
--------------------------
   
The project solves the problem of creating secure and customizable passwords.

Many users choose passwords that are too short or predictable. This program allows users to generate random passwords with different character types and lengths. By including uppercase letters, lowercase letters, numbers, and symbols, the generated passwords become stronger and harder to guess.

Technologies Used
-----------------
   
<ins>Python:</ins>

*Python* is the main programming language used to build the application. 

IDE used for this project: *PyCharm* (2025.3.2.1)

<ins>Tkinter:</ins>

*Tkinter* is used to create the graphical user interface. It allows the program to display checkboxes, spinboxes, buttons, and input fields so users can interact with the application easily.

Program Structure
-----------------
The program is divided into three Python files, each responsible for a different part of the program.

- *interface.py*

   This file creates the graphical user interface of the program.

   It includes:

   The main window

   Checkboxes for selecting character types

   Spinboxes for selecting the number of characters

   An entry field to display the generated password

   A button to generate the password

   This file manages the layout and user input controls.

- *parolchiki.py*

   This file contains the password generation algorithm.

   It defines the function:

   `generate_password(lowercase, numbers, uppercase, signs, num_1, num_2, num_3, num_4)`

   <ins>This function:</ins>

    *Defines sets of characters (letters, numbers, symbols).

    *Checks which character types are selected.

    *Randomly selects characters using choice().

    *Adds the characters to a list.

    *Randomizes the order using shuffle().

    *Joins the characters into a final password string.

    *The function then returns the generated password.

- *maiin.py*

   This file connects the user interface and password generator.
 
   It performs the following tasks:

    *Reads the user's selected options from the interface

    *Calls the password generation function

    *Displays the generated password in the entry field

    *When the user presses the "generate a password" button, the program runs the generate() function.

Inputs
------

The program receives input from the user through the graphical interface.

The inputs include:

  -Checkbox selections

  -Lowercase letters

  -Numbers

  -Uppercase letters

  -Special symbols

  -Spinbox values

  -Number of lowercase letters

  -Number of numbers

  -Number of uppercase letters

  -Number of symbols

These inputs determine the structure and length of the generated password.

Output
-------

The program outputs a randomly generated password.

The generated password is displayed in the entry field of the application window after the user clicks the generate button.

*Example output:*

**aF7!kP3@**

Algorithm Explanation
---------------------

The password generation algorithm works as follows:

 -Create an empty list called password.

 -Define four groups of characters:

   *lowercase letters

   *numbers

   *uppercase letters

   *special symbols

-For each selected character type:

  *Repeat according to the selected number.

  *Randomly choose a character from the corresponding group.

  *Add the character to the password list.

-Shuffle the list to randomize the order.

-Join the characters together into a single string.

-Return the final password.

This algorithm ensures the password follows the user's selected requirements while remaining random.

How Users Can Get Started
-------------------------

<ins>To use the program:</ins>

Run the `main.py` file.

The program window will open.

Select the character types using the checkboxes.

Choose the number of characters for each type using the spinboxes.

Click the "generate a password" button.

The generated password will appear in the entry field.

Users can repeat this process to generate new passwords.

