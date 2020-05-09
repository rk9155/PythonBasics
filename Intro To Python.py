#!/usr/bin/env python
# coding: utf-8

#  ## Intro To Jupiter
#  We can write markdown or python code in our cells

# In[4]:


a = 10;
print(a)


# In[5]:


print("hello")
print("hello")
x = 10
x = "String"
print(x)
print("x")


# ## Data Types Python

# In[6]:


a = 10
b = 10
c = a*b
c
print(c)


# In[9]:


a = 10
b = 10
a + b
10


# In[12]:


abc = 10
ab_c = 10
a_1 = 10
_a1 = 10
# 12a = 10


# In[15]:


print(type(a))
print(type(10))
type(1.0)


# In[18]:


a = 10
print(id(a))
a = a+1
#  number stored in different number
print(id(a))


# In[23]:


a = 10
id1 = id(a)
print(id1)
b = a + 2-2
id2 = id(b)
print(id2)


# ## arithmetic operator

# In[27]:


a = 10
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #integer divison


# In[28]:


print(a**b) #exponenetian  10^4
print(a%b)


# ## input from user python

# In[30]:


a = input()
a


# In[34]:


a = input()
b = input()
c = a + b
print(c)
print(type(c))


# In[40]:


b ='3.4'
a = int(b)
print(a)


# In[43]:


a = int(input())
print(a)
print(type(a))


# In[44]:


a = int(input())
b = int(input())
s = a+b
print(s)


# ## conditionals and loops

# In[3]:


a = True
b = "False"
print(type(a))
print(type(b))


# In[4]:


a = 10
b = 20
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)


# In[7]:


a = True
if a :
    print("i am inside if")
else :
    print("outside if")


# In[8]:


a = False
if a :
    print("inside if")
else :
    print("outside if")


# In[10]:


n = int(input())
if n>0 :
    print("Positive")
elif n<0 :
    print("Negative")
else :
    print("Zero")


# In[11]:


#while loop
n = int(input())
sum = 0
while n>0 :
    sum = sum + n;
    n = n-1
    
print(sum)


# In[12]:


n = int(input())
i = 0
sum = 0
while (i<=n) :
    if (i%2 == 0):
      sum+=i
    i = i+1

print(sum)


# In[39]:


inp = int(input())
if (inp == 1) :
    m = int(input())
    n = int(input())
    print(m+n)
elif (inp == 2) :
     m = int(input())
     n = int(input())
     print(m-n)
elif (inp == 3) :
     m = int(input())
     n = int(input())
     print(m*n)
elif (inp == 4) :
     m = int(input())
     n = int(input())
     print(m/n)
elif (inp == 5) :
     m = int(input())
     n = int(input())
     print(m%n)
elif (inp == 7) :
       print("Invalid Operation")
else :
    sys.exit()


# In[1]:


# Check Palindrome
def reverseDigits(num) :  
    rev_num = 0;  
    while (num > 0) : 
        rev_num = rev_num * 10 + num % 10
        num = num // 10
    return rev_num  
# Function to check if n is Palindrome 
def isPalindrome(n) : 
    # get the reverse of n  
    rev_n = reverseDigits(n);  
    # Check if rev_n and n are same or not.  
    if (rev_n == n) : 
        print("true")
    else : 
        print("false")

n = int(input())
isPalindrome(n)


# In[11]:


def sumE(n) : 
    st = str(n)
    sumEven = 0
    i = 0
    while(i<len(st)):
            sumEven+=int(st[i])
            i=i+2
    return sumEven

def sumO(n) : 
    st = str(n)
    sumOdd = 0
    i = 1
    while(i<len(st)):
            sumOdd+=int(st[i])
            i=i+2
    return sumOdd

n = int(input())
e = sumE(n)
o = sumO(n)
print(e, " " ,o)


# In[ ]:


def sumE(n) : 
    st = str(n)
    sumEven = 0
    i = 0
    while(i<len(st)):
        if(int(st[i])%2 == 0):
            sumEven+=int(st[i])
        i=i+1
    return sumEven

def sumO(n) : 
    st = str(n)
    sumOdd = 0
    i = 0
    while(i<len(st)):
         if(int(st[i])%2 != 0):
                sumOdd+=int(st[i])
         i=i+1
    return sumOdd

n = int(input())
e = sumE(n)
o = sumO(n)
print(e, " " ,o)


# In[1]:


# Progra to print nth fibo

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
    
n = int(input())
print(Fibonacci(n))


# ## Patterns problems
# 

# In[8]:


# ****
# ****
# ****
# ****

n = int(input())
i = 1
while i <= n  :
    j = 1
    while j <= n :
        print('*', end='')
        j = j + 1
#         print jth column
    print()
    i = i + 1


# In[10]:


n = int(input())
i = 1
while i <= n  :
    j = 1
    while j <= n :
        print(i, end='')
        j = j + 1
#         print jth column
    print()
    i = i + 1


# In[13]:


n = int(input())
i = 1
while i <= n :
    j = 1
    while j <= n :
        print(j, end='')
        j = j + 1
    print()
    i = i + 1


# In[15]:


# triangular patterns
n = int(input())
i = 1
while(i<=n):
    j = 1
    while(j<=i):
        print(j, end='')
        j = j+1
    print()
    i = i+1


# In[17]:


n = int(input())
i = 1
while(i<=n):
    j = 1
    p = i
    while(j<=i):
        print(p, end='')
        j = j+1
        p = p+1
    print()
    i = i+1


# In[21]:


# Character Patterns

n = int(input())
i = 1
while i <= n :
    j = 1
    while j <= n :
#         find next character using ascii
        charP = chr(ord('A') + j - 1)
        print(charP, end='')
        j = j + 1
    print()
    i = i + 1


# In[24]:


n = int(input())
i = 1
while i <= n :
    j = 1
    startChar = chr(ord('A') + i - 1)
    while j <= n :
#         find next character using ascii
        charP = chr(ord(startChar) + j - 1)
        print(charP, end='')
        j = j + 1
    print()
    i = i + 1


# In[27]:


# reverse patterns
n = int(input())
i = 1
while(i<=n):
    j = 1
    while(j <= n-i+1):
        print("*", end="")
        j = j + 1
    print()
    i = i+1


# In[29]:


# Reversed and Inverted Pattern
n = int(input())
i = 1
while(i<=n):
    spaces = 1
    while(spaces <= n-i):
        print(' ', end="")
        spaces = spaces+1
    stars = 1
    while(stars<=i):
        print("*", end="")
        stars = stars + 1
    print()
    i = i+1


# In[31]:


# Isosceles Pattern

n = int(input())
i = 1
while(i<=n):
    spaces = 1
    p =1
    while(spaces <= n-i):
        print(' ', end="")
        spaces = spaces+1
    stars = 1
    while(stars<=i):
        print(p, end="")
        stars = stars + 1
        p = p+1
    print()
    i = i+1


# In[32]:


n = int(input())
i = 1
while(i<=n):
    spaces = 1
    p =1
#     spaces
    while(spaces <= n-i):
        print(' ', end="")
        spaces = spaces+1
    stars = 1
#     //increasing sequences
    while(stars<=i):
        print(p, end="")
        stars = stars + 1
        p = p+1
#     decreasing sequnese
    p = i-1
    while(p>=1):
        print(p,end="")
        p = p-1
    
    print()
    i = i+1


# In[38]:


# Diamond Pattern
n = int(input())
i = 1
while(i<=n):
    spaces = 1
    p =1
#     spaces
    while(spaces <= n-i):
        print(' ', end="")
        spaces = spaces+1
    stars = 1
#     //increasing sequences
    while(stars<=i):
        print("*", end="")
        stars = stars + 1
        p = p+1
#     decreasing sequnese
    p = i-1
    while(p>=1):
        print("*",end="")
        p = p-1
    
    print()
    i = i+1


# In[42]:


rows = int(input())
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")


# In[49]:


n = int(input())
rows = n//2 + 1
 
#top half
k = 0
for i in range(1, rows + 1): 
    # print spaces 
    for j in range (1, (rows - i) + 1): 
        print(end = " ") 
	  
        # let's print stars 
    while k != (2 * i - 1):
        print("*", end = "")
        k = k + 1
    k = 0
	  
    # add a line break 
    print()  
 
#bottom half
k = 2
m = 1
for i in range(1, rows): 
    # print spaces 
    for j in range (1, k):
        print(end = " ") 
    k = k + 1
	  
    # print star 
    while m <= (2 * (rows - i) - 1): 
        print("*", end = "") 
        m = m + 1
    m = 1
	
    #add a line break
    print() 


# ## More On Loops for loop
# 

# In[51]:


s = "Rakesh"
for c in s:
    print(c)


# In[52]:


# range(start,end,strive)
n = int(input())
for i in range(0, n, 1):
    print(i)


# In[53]:


n = int(input())
for i in range(n+1):
    print(i)


# In[54]:


n = int(input())
for i in range(1,n+1):
    print(i)


# In[55]:


# print multiples of 3
a = int(input())
b = int(input())
for i in range(a,b+1,1):
    if i % 3 == 0 :
        print(i)


# In[58]:


n = int(input())
for i in range(1,n+1,1):
    for s in range(n-i):
        print(" ", end="")
    for j in range(i,2*i,1):
        print(j,end="")
    for j in range(2*i - 2,i-1,-1):
        print(j,end="")
    print()


# ## break

# In[60]:


i = 1
while(i<=10):
    if(i==5) :
        break
    print(i)
    i = i + 1


# In[63]:


# Square Root
def Sqrt(x): 
    if (x == 0 or x == 1): 
        return x 
# Staring from 1, try all numbers until 
    # i*i is greater than or equal to x. 
    i = 1; result = 1
    while (result <= x): 
        i += 1
        result = i * i 
    return i - 1
 
n = int(input())
print(Sqrt(n))


# In[64]:


# Decimal to Binary

def DecimalToBinary(num): 
      
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2, end = '') 

n = int(input())
DecimalToBinary(n)


# In[67]:


# Binary to decimal

  
def binaryToDecimal(binary):    
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    print(decimal)    
n = int(input())
binaryToDecimal(n)


# In[2]:


# Even Fibonacci
n = int(input())
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
sum = 0
for i in range(1,n,1):
    x = Fibonacci(i)
    if x<=n :
        if x % 2 == 0 :
            sum+=x
    else :
        break
            
print(sum)
        


# In[ ]:


# Trailing zeroes in n!
n = int(input())
sum = 0
r = 1
while(r<=5):
    r = n//5
    sum+=r
print(sum)
    


# In[ ]:




