#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input())
equalSign = '='
cross = 'x'
space = ' '
for x in range (1 , 11):
        print(str(n) +space + cross + space +str(x)+ space + equalSign +space + str(n * x ))
      #  print("\n")
        
