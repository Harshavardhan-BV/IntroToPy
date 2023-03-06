# Tutorial 05
(15 marks)

Reading and understanding code is just as important as writing code ([Relevant Meme](https://www.reddit.com/r/ProgrammerHumor/comments/11he9yl/age_old_truth_dont_underestimate_code_readability/)). 

Given is the [PlagiarismCheck.py](./PlagiarismCheck.py) file, which is used to calculate the similarity score between python files. Have a look and give a detailed step-by-step explanation of how the python code operates. You may refer to the documentation of the respective modules/functions.

You may write these as comments in the python file itself. Otherwise, write it in a text/word/pdf document.

Example outputs are in the [Output](./Output/) folder. If you want to run the code for yourself, ask your friends for their python codes from previous assignments (if you have not already :P) and add ' - name' to the end of the file.

Note: The python code calls *nix shell commands like `comm` and `wc`. Brief descriptions of them are as follows: 
- `comm -12 file1.py file2.py` print the lines present in both file1.py and file2.py by comparing line by line
- `command1 | command2` is piping the output from command1 to the input of command2
- `wc -l file.py` prints the count of the number of lines in file.py
