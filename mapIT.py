#! python3
# Mapit gets a map from your web browser
#from Automate the Boring Stuff
#comand line or clipboard


import sys, webbrowser, pyperclip
if len(sys.argv) > 1:
    #get address from comand line.
    address = ''.join(sys.argv[1:])
else:
    #Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


#TODO:  Read the command line arguments from sys.argv.



#TODO:  Read the clipboard contents.


#TODO:  Call the webbrowser.open() function to open the web browser.

#i dont knwo wht athe fuck happened to mh pypercclip or pyperclip
