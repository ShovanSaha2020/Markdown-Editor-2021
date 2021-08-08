# Markdown-Editor-2021
## JetBrains Academy Project | Level :  Medium

### About
Markdown is a special plain text formatting language that is extremely popular among developers. It is used in documents, research articles, Github README files, and other things. In this project, I have created an editor that can recognize several tags, structures, and save the results to a file.

The program works in the following way:
It will ask the user to input a formatter.
If the formatter doesn't exist, it will print the following error message: "Unknown formatting type or command."
Then it will ask the user to input a text that will be applied to the formatter.
It will save the text with the chosen formatter applied to it and print the markdown after that. Each time the program will print out the whole text in markdown accumulated so far.
Available formatters:
plain — a normal text without any formatting
bold/italic — self-explanatory
inline-code — for example, python editor.py
link — for example, google.com
header — look at the header of this stage.
unordered-list — this very list is an example of an 					unordered list
ordered-list — a list with enumerated elements
new-line — switches to the next line
	6. Special commands:
!help — prints available syntax commands.
!done — saves the results to a file and exits the app.

Different formatters may require different inputs.




### Example Outputs:
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.
##### Example 1: 
```
Choose a formatter: > non-existing-formatter
Unknown formatter type or command
Choose a formatter: > header
Level: > 4
Text: > Hello World!
#### Hello World!

Choose a formatter: > plain
Text: > Some plain text
#### Hello World!
Some plain text
Choose a formatter: > new-line
#### Hello World!
Some plain text

Choose a formatter: > link
Label: > Tutorial
URL: > https://www.markdownguide.org/basic-syntax/
#### Hello World!
Some plain text
[Tutorial](https://www.markdownguide.org/basic-syntax/)
Choose a formatter: > !done
```
##### Example 2:
```
Choose a formatter: > ordered-list
Number of rows: > 3
Row #1: > First element
Row #2: > Second element
Row #3: > Third element
1. First element
2. Second element
3. Third element

Choose a formatter: > unordered-list
Number of rows: > 2
Row #1: > Fourth element
Row #2: > Fifth element
1. First element
2. Second element
3. Third element
* Fourth element
* Fifth element

Choose a formatter: > unordered-list
Number of rows: > -2
The number of rows should be greater than zero
Number of rows: > 2
Row #1: > Sixth element
Row #2: > Seventh element
1. First element
2. Second element
3. Third element
* Fourth element
* Fifth element
* Sixth element
* Seventh element

Choose a formatter: > !done
```

##### Example 3: 
```
Choose a formatter: > header  
Level: > 1  
Text: > Hello World!  
# Hello World!  
  
Choose a formatter: > plain  
Text: > Lorem ipsum dolor sit amet, consectetur adipiscing elit  
# Hello World!  
Lorem ipsum dolor sit amet, consectetur adipiscing elit  
Choose a formatter: > line-break  
# Hello World!  
Lorem ipsum dolor sit amet, consectetur adipiscing elit  
  
Choose a formatter: > ordered-list  
Number of rows: > 3  
Row #1: > dolor  
Row #2: > sit  
Row #3: > amet  
# Hello World!  
Lorem ipsum dolor sit amet, consectetur adipiscing elit  
1. dolor  
2. sit  
3. amet  
  
Choose a formatter: > !done 
```

