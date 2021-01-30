import os

'''
pyaltername
________________________________________________________
| Author : Michael Amadi (Mgregchi)                       |
| Email : mgregchi@gmail.com                                 |
| Url : https://github.com/Mgregchi/pyaltername/  |
|_______________________________________________________|
'''

'''
PLEASE RUN THIS PROGRAM AS ROOT (ADMIN)
TO AVOID "Access is denied" ERROR.
How to:
Open command prompt (shell) as An admin or root.
cd >> test
run acording to your OS

py test.py OR
test.py OR
python3 test.py OR

pyaltername test program
If test fails please create an issue on github
Using the URL above.

Hint : Open  ' test ' directory with your system file
manager and watch as dummy file is created,
renamed and deleted, to further confirm everything is working fine.

You can Add further tests and submit pull request.
'''

import os
import time


try:
        import pyaltername as palt
except ImportError as err:
        print("An error occured please resolve before procceding :::   ", err)
        raise 
        
ERROR = []



# Test Generic
print("Checking name()... ")
try:
        gen = palt.Generic()
        result = gen.name("app.py", os.getcwd())
        print("name() results  :::\n    ", result)
except Exception as err:
        print("""Error occured with 'Generic' >> 'name'
        Make sure pyaltername is installed properly and not broken.:::   """, err)
        ERROR.append("Generic >> name")

print("\nChecking Generic.rename() ::: \n")

try:
        dummy = open("dummy.txt", "w")
        print("Dummy file created")
        dummy.close()
        time.sleep(3)
        gen.rename(src = "dummy.txt",
                dst = "renamed_dummy.txt",
                path = os.getcwd(),
                jump_extension = ["py"]
        )
        
except Exception as err:
        print("rename failed ::  ", err)
        ERROR.append("Generic >> rename")

time.sleep(3)

find = palt.Find()

print("Checking Find.file_name() :::\n")

try:
        status = find.file_name("renamed_dummy.txt",
                       path = os.getcwd()
                       )
        print("File found ::  ", status)
except Exception as err:
        print("Find.file_name() failed  :::    ", err)
        ERROR.append("Find >> file_name")

print("Attenpting to locate files that ends with '.py'\n in this directory using [Find._filename()] :::: \n")

try:
        py_files = find.file_extension(".py",
                            path = os.getcwd()
                        )
        print("find.file_extension results  ::\n     ", py_files)
except Exception as err:
        print("Error :: Find()  ", err)
        ERROR.append("Find >> file_extension")

print("prepaing results ... \n")
#time.sleep(4)

if ERROR:
        for error in ERROR:
                print(error)
else:
        print("No issues found!")
print("Test done.")
os.remove("renamed_dummy.txt")
