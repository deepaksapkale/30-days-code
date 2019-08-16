#!/bin/python3

import math
import os
import random
import re
import sys


N = int(input())
mod = int(N % 2)
if( mod > 0):
        print("Weird")
elif(mod == 0 and  (N >= 2 or N >= 5 )):
        print("Not Weird")
elif(mod == 0 and  (N >= 6 or N <= 20 )):
        print("Weird")
elif(mod == 0 and  N > 20):
        print("Not Weird")