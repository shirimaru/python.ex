def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*factorial(n-1)
while True:
  try:
    n = int(input("Enter your number:"))
    print(f"{n}! = {factorial(n)}")
    break
  except Exception as e:
    print("Please enter integer values only.")
        


