import time

def clock(t):
  c = 0
  while(c!=t):
    c+=1
    time.sleep(60000) ##Mins
   return c
