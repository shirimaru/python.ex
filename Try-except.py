while True:
  n = input("Enter your number:")
  try:
   print(f"The table of {int(n)} is as follows:")
   for i in range(1,11):
     print(f"{int(n)} x {i}={int(n)*i}")
   break  
  except Exception as   a:
    print("please enter the interger values only ")
 
 
 
 

  
    
