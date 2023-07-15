#!/usr/bin/env python
# coding: utf-8

# # Question 1- Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

# In[1]:


import re

def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)
print(is_allowed_specific_char("ABCDEFabcdef123450"))#true
print(is_allowed_specific_char("*&%@#!}{"))


# # Question 2- Create a function in python that matches a string that has an a followed by zero or more b's

# In[2]:


import re
def text_match(text):
    patterns = '^a(b*)$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))


# # Question 3-  Create a function in python that matches a string that has an a followed by one or more b's

# In[4]:


import re
def text_match(text):
    patterns = 'ab+?'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')
    
print(text_match("ab"))
print(text_match("abc"))
        


# # Question 4- Create a function in Python and use RegEx that matches a string that has an a followed by zero or one 'b'.

# In[5]:


import re
def text_match(text):
    patterns = 'ab?'
    if re.search(patterns, text):
        return "Found a match!"
    else:
        return ("Not matched!")

print(text_match("ab"))

print(text_match("abc"))

print(text_match("abbc"))

print(text_match("aabbc"))    


# # Question 5- Write a Python program that matches a string that has an a followed by three 'b'.

# In[8]:


import re
def text_match(text):
    patterns = "ab{3}?"
    if re.search(patterns, text):
        return "Found a match!"
    else:
        return("Not matched!")
    
print(text_match("abbb"))
print(text_match("aabbbbbc"))
print(text_match("aabc"))


# # Question 6- Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”
# Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]
# 

# In[9]:


import re
text = "ImportanceOfRegularExpressionsInPython"
print(re.findall('[A-Z][^A-Z]*', text))


# # Question 7- Write a Python program that matches a string that has an a followed by two to three 'b'.

# In[10]:


import re
def text_match(text):
    patterns = "ab{2,3}"
    if re.search(patterns, text):
        return "found a match!"
    else:
        return("not matched")
    
print(text_match("ab"))
print(text_match("aabbbbbbc"))
print(text_match("aabbbbbbccc"))


# # Question 8- Write a Python program to find sequences of lowercase letters joined with a underscore.

# In[11]:


import re
def text_match(text):
    patterns = "^[a-z]+_[a-z]+$"
    if re.search(patterns, text):
        return "Found a match!"
    else:
        return("not matched!")
    
print(text_match("aab_cbbbc"))
print(text_match("aab_abbbbc"))
print(text_match("Aabbb_abbbccc"))
    
    
        


# # Question 9- Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# In[13]:


import re
def text_match(text):
    patterns = "a.*?b$"
    if re.search(patterns, text):
        return "Found a match!"
    else:
        return("Not matched!")
    
print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjb"))
print(text_match("abbb"))


# # Question 10- Write a Python program that matches a word at the beginning of a string.

# In[14]:


import re
def text_match(text):
    patterns = "^\w+"
    if re.search(patterns, text):
        return "Found a match!"
    else:
        return("Not matched!")
    
print(text_match("I love to have chocolates"))
print(text_match("I love to have chocolates"))
    


# # Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[15]:


import re
def text_match(text):
    patterns = "^[a-zA-z0-9_]*$"
    if re.search(patterns, text):
        return "Found a match!"
    else:
        return("Not matched")
    
print(text_match("I love to have chocolates"))
print(text_match("love_CadburyDairymilkChocolates_1"))
    


# # Question 12- Write a Python program where a string will start with a specific number. 

# In[16]:


import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
    
print(match_num("5-1234567"))
print(match_num("9-1234567"))


# # Question 13- Write a Python program to remove leading zeros from an IP address

# In[17]:


import re
ip = "103.159.251.75"
string = re.sub("\.[0]*",".",ip)
print(string)


# # Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# Sample text : ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
# 
# 

# In[18]:


import re
regex = r"([a-zA-Z]+) (\d{1,2}), (\d{4})"
test = "August 15, 1947"
matches = re.search(regex, test)

if matches:
    print(matches.group())


# # Question 15- Write a Python program to search some literals strings in a string. Go to the editor
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
# 

# In[21]:


import re
patterns = ['fox','dog','horse']
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' %(pattern, text),)
    if re.search(pattern,text):
        print("Matched!")
    else:
        print("Not Matched!")


# # Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
# 

# In[22]:


import re
pattern = "fox"
text = "The quick brown fox jumps over the lazy dog."
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s in "%s" from %d to %d ' % 
     (match.re.pattern, match.string, s, e))


# # Question 17- Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'.
# 

# In[23]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = "exercises"
for match in re.findall(pattern, text):
    print('Found "%s"' % match)


# # Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

# In[25]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = "exercises"
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    
    print('Found "%s" at %d:%d' % (text[s:e],s,e))


# # Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[26]:


import re
def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1="2023-07-13"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


# # Question 20- Write a Python program to find all words starting with 'a' or 'e' in a given string.

# In[27]:


import re
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
list = re.findall("[ae]\w+", text) #find all the words starting with 'a' or 'e'
print(list)


# # Question 21- Write a Python program to separate and print the numbers and their position of a given string.

# In[28]:


import re
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
for k in re.finditer("\d+", text):
    print(k.group(0))
    print("index position:", k.start())


# # Question 22- Write a regular expression in python program to extract maximum numeric value from a string

# In[29]:


import re

string="ab12cd123ef23"
pattern = r'\d+'
numbers = re.findall(pattern, string)
max_num = max(map(int, numbers))
print(max_num)   


# # Question 23- Write a Regex in Python to put spaces between words starting with capital letters

# In[30]:


import re 

text="ThisIsAStringWithWordsStartingWithCapitalLetters"

new_text = re.sub(r'(?<!^)(?=[A-Z])',' ', text)

print(new_text)


# # Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

# In[31]:


import re
def text_match(text):
    patterns = '[A-Z]+[a-z]+$'
    if re.search(patterns, text):
        return "Found a match!"
    else:
        return("Not matched!")
    
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("ABCD"))
print(text_match("aA"))
print(text_match("Aa"))


# # Question 25- Write a Python program to remove duplicate words from Sentence using Regular Expression

# In[32]:


import re

def removeDuplicatesFromText(text):
    regex = r'\b(\w+)(?:\W+\1\b)+'
    return re.sub(regex, r'\1', text, flags=re.IGNORECASE)

str1 = "How are are you"
print(removeDuplicatesFromText(str1))

str2 ="Programming is fun fun"
print(removeDuplicatesFromText(str2))

str3 = "Remove duplicate words from from text"
print(removeDuplicatesFromText(str3))


# # Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

# In[34]:


import re

regex_expression = '[a-zA-Z0-9]$'

def check_string(my_string):
    if(re.search(regex_expression, my_string)):
        print("The string ends with an alphanumeric character")
    else:
        print("The string does not end with an alphanumeric character")
        
my_string = "Hello world 123"
check_string(my_string)


# # Question 27-Write a python program using RegEx to extract the hashtags.
# Sample Text: text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
# Output: ['#Doltiwal', '#xyzabc', '#Demonetization']
# 

# In[42]:


import re
string = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
pattern ="#\w+"
hashtags = re.findall(pattern, string)
print(hashtags)


# # Question 28- Write a python program using RegEx to remove <U+..> like symbols
# Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
# Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
# Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders
# 

# In[43]:


import re

string = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

pattern = '<.*?>'

replace = ''

new_string = re.sub(pattern, replace, string)

print(new_string)


# # Question 29- Write a python program to extract dates from the text stored in the text file.
# Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
# Store this sample text in the file and then extract dates.
# 

# In[48]:


import re
content ="(Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.)"
("Store this sample text in the file and then extract dates")
pattern ="\d{2}[/-]\d{2}[\-]\d{4}"
dates = re.findall(pattern, content)

for date in dates:
    if "-" in date:
        day, month, year = map(int, date.split("-"))
    else:
        day, month, year = map(int, date.split("/"))
    if 1 <= day <= 31 and 1 <= month <= 12:
        print(date)
        


# # Question 30- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Sample Text- 'Python Exercises, PHP exercises.'
# Output: Python:Exercises::PHP:exercises:
# 

# In[49]:


import re

text="Python Exercises, PHP exercises."

print(re.sub("[ ,.]", ":", text))


# In[ ]:




