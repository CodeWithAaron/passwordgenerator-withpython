import random

lower = "abcdefghijklmnopqrstuvwzyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_-"

     all = lower + upper + number + symbols
     length = 16
     password = "".join(random.sample(all,length))
     print "password"
