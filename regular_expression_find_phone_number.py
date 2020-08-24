
#phone number checker useing re Module
#code from Al Sweigart's Automate the Boring Stuff Udemy course.

import re
#regular expressions

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me at 415-555-1011 tomorrow, or at 415-123-4587 which is my office number. ')# mo stands for matched objects
print(mo.group())
#I get a traceback that says there is no group attribute when I use findall
