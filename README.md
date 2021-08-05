# Markdown-Editor-2021
## JetBrains Academy Project | Level :  Medium

### About
Markdown is a special plain text formatting language that is extremely popular among developers. It is used in documents, research articles, Github README files, and other things. In this project, I have created an editor that can recognize several tags, structures, and save the results to a file.

### Example Outputs:
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.
##### Example 1: 
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

