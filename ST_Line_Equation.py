x1, y1 = input("Enter the Value of (x1, y1) :").split()
x2, y2 = input("Enter the Value of (x2, y2) :").split()

x1, y1 = int(x1), int(y1)
x2, y2 = int(x2), int(y2)

dx,dy  = x2 - x1, y2 - y1

print(f"\nEquation of line passing through ({x1},{y1}) and ({x2},{y2}) is:")

if ( dy % dx == 0 ):
   dy//= dx 
   dx = 1
elif ( dx % dy == 0 ):
   dx//= dy 
   dy = 1
else:
   if (dx < dy ):
      max = dx
   else:
      max = dy
   
   for divisor in range(2, max + 1):
      if ( dy % divisor == 0 and dx % divisor == 0):
         dy//= divisor
         dx//= divisor
         break
      else:
         pass

A , B = dy , dx 
cons = dx * y1 - x1 * dy

# Value of dx, dy and Cons is updated accrodingly..

if( A > 0 and B > 0 ):
   if (A == 1): 
      A_str = "X" 
   else: 
      A_str = f"{A}X" 
   if (B == 1): 
      B_str = " - Y" 
   else: 
      B_str = f" - {B}Y" 
   if (cons > 0): 
      cons_str = f" + {cons} = 0" 
   elif(cons < 0): 
      cons_str = f" = {-cons}" 
   else:
      cons_str = " = 0"

elif( A > 0 and B < 0 ):
   if (A == 1):
      A_str = "X"
   else:
      A_str = f"{A}X"
   if(B == -1):
      B_str = " + Y"
   else:
      B_str = f" + {-B}Y"
   if(cons > 0):
      cons_str = f" + {cons} = 0"
   elif(cons<0):
      cons_str = f" = {-cons}"
   else:
      cons_str = " = 0"

elif( A < 0 and B > 0 ):
   if (A == -1):
      A_str = "X"
   else:
      A_str = f"{-A}X"
   if(B == 1):
      B_str = " + Y"
   else:
      B_str = f" + {B}Y"
   if(cons > 0):
      cons_str = f" = {cons}"
   elif(cons < 0):
      cons_str = f" + {-cons} = 0"
   else:
      cons_str = " = 0"

else:
   if (A == -1):
      A_str = "X"
   else:
      A_str = f"{-A}X"
   if(B == -1):
      B_str = " - Y"
   else:
      B_str = f" - {-B}Y"
   if(cons>0):
      cons_str = f" = {-cons}"
   elif(cons < 0):
      cons_str = f" + {-cons} = 0"
   else:
      cons_str = " = 0"

print(f"{A_str}{B_str}{cons_str}")