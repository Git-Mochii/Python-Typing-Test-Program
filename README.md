# Python-Typing-Test-Program

This is a typing test program I made in Python.

The purpose of this program is to make the user accurately type and copy sentences that are displayed so that their wpm (word per minute) can be calculated. 

The program begins by prompting the user to make three decisions:
- 'start' - which will initialize the rest of the program
- 'scores' - which will display the user's top scores of that session
- 'exit' which will quit the program and output the appropriate message

If the user selected 'start' then the next part of the program collects the user details for the test. The user will need to input their name which can be either
numbers or letter characters and afterwards, they will be asked to input the current date that they are taking the test - the date must be formatted in (d/m/y).

Once the user details have been collected, a quick guide message will output telling the user how to complete the test. Immediately, after this message appears
a 5-second countdown begins; at the end of this countdown the test will have begun and the first sentence will have appeared for the user to type. Sentences
must be accurately typed out with proper grammar, failure to do so will cause the program not to count the wpm and point for that particular sentence; additionally,
for user-friendly purposes, the appropriate message will appear depending on whether the user scored a point or if they had made a mistake and add on a 4-second penalty.

After all the sentences have been completed, the program will output:
- The total score
- The time taken to complete the test
- The total wpm
- The average wpm 
(This information as well as the date is appended to the top scores)

At the end of the program, the user will be asked to either type:
- play - which will start the program from the beginning
- scores - which will display the top scores list containing the user name, the total score of that user, the date of the test and the wpm
- exit - which will quit the program and display the appropriate message

---------
[Imported repo from old account]
---------
