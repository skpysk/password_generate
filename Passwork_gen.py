import string
import random

x = string.ascii_lowercase
y = string.ascii_uppercase
z = string.digits
r = string.punctuation
while True :   # always use while loop for this always ask for input also try your code run 
  try:
   lenght = int(input("Enter Your Lenght Of Password  :  ")) # if someone input anything so use try to indicate user with message

  except ValueError:
        print(" Plz Enter a valid lenght of password which do you want to generate")
  else:
    print("sorry we can not able to generate") # this is choice
    break


x1 = []
                    # appen direct utha ker daal deta he like [1,2] list ko he dal dega but jaw ham alg alg 1, or 2 ko add krna chte he like [5,6,1,2] ek list me he ayega
x1.extend(x)
x1.extend(y)
x1.extend(z)
x1.extend(r)

# if we want conbert a string in split way like abcd in ['a', 'b', 'c', 'd'] so use list(s) where s is holding your string
random.shuffle(x1)
print("your password 1 is :  ","".join(x1[0:lenght]))  # using "".join bcz x1[0:lenght] give us list like ['i','5', '&'] so but we need i5& so this is why we use "".join if we put some thing in "any thing". join will join with it like "2".join i(2)5(2)& like this in () braket
print("your password 2 is : ","".join(random.sample(x1, lenght)))