# Overriding_Extension

Use:
The purpose of overriding an extension is to display a different extension than the base or original one.
Attackers uses this method to deliver malicious files

Logic/Method:
Override characters can be used to change the display of file extensions from Right-To-Left (RTL) or Left-To-Right (LTR).
In this method, the Right-To-Left Override character (U+202E) is employed.
For example, if you have a file named Try.txt and you want to change its extension to .pdf, you would reverse the extension and insert the RTL Override character before it.
So, to convert Try.txt to .pdf, you would rename the file to Tryfpd.txt and insert the RTL Override character before the 'f'. This will make the file appear as Trytxt.pdf

This method can be lengthy and prone to mistakes, so I created a Tkinter Python program that automates the process of renaming file extensions using the override technique.(File override_file_extension.py)
