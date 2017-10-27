infoKivy.txt

# Overview
A fork of https://github.com/kivy/kivy

# TODO
Windows PH Library right install per
    https://keep.google.com/#NOTE/15f5e3a4640.aecc194148ecde0f
    gets "ModuleNotFoundError: No module named 'kivy._clock'" too.

    terminal
    pushd C:\Users\Resident.2Y28GZ1-PH\PycharmProjects\kivy\examples\widgets\recycleview
    C:\Users\Resident.2Y28GZ1-PH\AppData\Local\Programs\Python\Python36\python basic_data.py
    "ModuleNotFoundError: No module named 'kivy'"


Look through examples/widgets/recycleview/basic_data.py to figure out how to implement MVC.

python2 & python3 get the same "No module named 'kivy._clock'"
/usr/bin/python3.5 /home/dalem/PycharmProjects/kivy/examples/widgets/recycleview/basic_data.py
[WARNING] [Config      ] Older configuration version detected (19 instead of 20)
[WARNING] [Config      ] Upgrading configuration in progress.
[DEBUG  ] [Config      ] Upgrading from 19 to 20
[INFO   ] [Logger      ] Record log in /home/dalem/.kivy/logs/kivy_17-10-23_4.txt
[INFO   ] [Python      ] v3.5.2 (default, Sep 14 2017, 22:51:06) 
[GCC 5.4.0 20160609]
 Traceback (most recent call last):
   File "/home/dalem/PycharmProjects/kivy/examples/widgets/recycleview/basic_data.py", line 4, in <module>
     from kivy.app import App
   File "/home/dalem/PycharmProjects/kivy/kivy/app.py", line 319, in <module>
     from kivy.base import runTouchApp, stopTouchApp
   File "/home/dalem/PycharmProjects/kivy/kivy/base.py", line 26, in <module>
     from kivy.clock import Clock
   File "/home/dalem/PycharmProjects/kivy/kivy/clock.py", line 362, in <module>
     from kivy._clock import CyClockBase, ClockEvent, FreeClockEvent, \
 ImportError: No module named 'kivy._clock'

I'd had this problem in PyCharm but not command line and asked JetBrains about this:
kivy examples https://github.com/kivy/kivy/tree/master/examples/widgets/recycleview don't work in PyCharm because they get "ImportError: No module named 'kivy._clock'"; but, examples run from the command line work fine.
https://mail.google.com/mail/u/0/#search/kivy._clock/15f17e7b7a7e1fcc
https://intellij-support.jetbrains.com/hc/requests/1107821
Run check_python_interpreter.py script from same interpreter and submit results.
Submitted
cpi_2_cl.log = check_python_interpreter.py python2 command line
cpi_3_cl.log = check_python_interpreter.py python3 command line
cpi_2_pc.log = check_python_interpreter.py python2 PyCharm
cpi_3_pc.log = check_python_interpreter.py python2 PyCharm
for JetBrains evaluation. Waiting to hear from them.


# Logs
###### Monday 23 October 2017 6:01 PM CST
Created
