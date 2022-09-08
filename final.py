# Funtion to seperate
num = int(input("Enter number:"))

def splitevenodd_(A): 
   evenlist = [] 
   oddlist = [] 
   for i in (A): 
      if (i % 2 == 0) and (i !=0):
         evenlist.append(i) 
      else: 
         oddlist.append(i) 
   print("Even lists:", evenlist) 
   print("Odd lists:", oddlist) 
splitevenodd_(A)