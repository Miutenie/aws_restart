import re
# read the content of the .txt file
with open('preproinsulin-seq1.txt', 'r') as file:
    content = file.read()
    
print(content)    

# use regex to find lowercase words
#r'\b[a-z]+\b'- is a regular expression checking for one or more lowercase letters '[a-z'
#bounded by word boudaries ('\b'). this pattern returns only the complete lowercase words
#re.findall() used to find all matches

lowercase_words = re.findall(r'\b[a-z]+\b', content)
print(lowercase_words)