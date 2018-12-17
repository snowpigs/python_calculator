
# coding: utf-8

# In[ ]:

#   _ _ _ _
#  |^ < ^ |
# <       >
# |       |

import time

def calculator():
    try:
        num1 = float(input("Input a number: "))
        time.sleep(0.5)
        un = str(input("Input a operation \n addition = + \n subtraction = - \n division = / \n multiplication = * \n"))
        time.sleep(0.5)
        num2 = float(input("input a number: "))
        time.sleep(0.5)
        if un == ("+"):
            num3 = num1 + num2
            print("\n", num1, "+", num2, "= ", num3)
        elif un == ("-"):
            num3 = num1 - num2
            print("\n", num1, "-", num2, "= ", num3)
        elif un == ("*"):
            num3 = num1*num2
            print("\n", num1, "x", num2, "= ", num3)
        elif un == ("/"):
            mum3 = num1/num2
            print("\n", num1, "÷", num2, "= ", num3)
        else:
            print("That is not an operation\nStarting over\n-------------------")
            time.sleep(1)
            calculate()
    except: 
        print("that is not a proper input")
        calculator()

def tryagain():
    num5 = 0
    again = str(input("Do you calculate more Y = yes N = no "))
    if again == ("Y") or again == ("y"):
        un2 = str(input("What is your next operation: "))
        num4 = float(input("what is your next number: "))
        if un2 == ("+"):
            num5 = num3 + num4
            print("\n", num3, "+", num4, "= ", num5)
            num3 = num5
            tryagain()
        elif un2 == ("-"):
            num5 = num3 - num4
            print("\n", num3, "-", num4, "= ", num5)
            num3 = num5
            tryagain()
        elif un2 == ("*"):
            num5 = num3*num4
            print("\n", num3, "x", num4, "= ", num5)
            num3 = num5
            tryagain()
        elif un2 == ("/"):
            num5 = num3/num4
            print("\n", num3, "÷", num4, "= ", num5)
            num3 = num5
            tryagain()
    elif again == ("N") or again == ("n"):
        print("OK")
    else:
        print("Not a correct response")
        tryagain()


# In[ ]:


calculator()
tryagain()


# In[1]:


get_ipython().run_line_magic('timeit', 'sum(range(100))')


# In[4]:


import numpy as np

