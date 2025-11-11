# Word Counter & Duplicate Finder 

A small Python script that reads a text file, counts the total words, and finds duplicate entries using `collections.Counter`.

##  Features
- Counts total words in a file  
- Detects duplicate words  
- Prints all word frequencies  
- Simple, readable logic — great for beginners learning file handling

##  How to Use
1. Clone or download this repository.
2. Replace the file path inside the script with your own `.txt` file:
   ```python
   with open("C:\\path\\to\\your\\file.txt", "r") as file:
       text = file.read()
