 ## Intro To Jupiter
 We can write markdown or python code in our cells


```python
a = 10;
print(a)
```

    10



```python
print("hello")
print("hello")
x = 10
x = "String"
print(x)
print("x")
```

    hello
    hello
    String
    x


## Data Types Python


```python
a = 10
b = 10
c = a*b
c
print(c)
```




    100




```python
a = 10
b = 10
a + b
10
```




    10




```python
abc = 10
ab_c = 10
a_1 = 10
_a1 = 10
# 12a = 10
```


```python
print(type(a))
print(type(10))
type(1.0)
```

    <class 'int'>
    <class 'int'>





    float




```python
a = 10
print(id(a))
a = a+1
#  number stored in different number
print(id(a))

```

    4549449120
    4549449152



```python
a = 10
id1 = id(a)
print(id1)
b = a + 2-2
id2 = id(b)
print(id2)
```

    4549449120
    4549449120


## arithmetic operator


```python
a = 10
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #integer divison
```

    14
    6
    40
    2.5
    2



```python
print(a**b) #exponenetian  10^4
print(a%b)
```

    10000
    2


## input from user python


```python
a = input()
a
```

    23





    '23'




```python
a = input()
b = input()
c = a + b
print(c)
print(type(c))
```

    23
    23
    2323
    <class 'str'>



```python
b ='3.4'
a = int(b)
print(a)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-40-d5cccde13f49> in <module>
          1 b ='3.4'
    ----> 2 a = int(b)
          3 print(a)


    ValueError: invalid literal for int() with base 10: '3.4'



```python
a = int(input())
print(a)
print(type(a))
```

    23
    23
    <class 'int'>



```python
a = int(input())
b = int(input())
s = a+b
print(s)
```

    23
    23
    46


## conditionals and loops


```python
a = True
b = "False"
print(type(a))
print(type(b))
```

    <class 'bool'>
    <class 'str'>



```python
a = 10
b = 20
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

```

    False
    True
    False
    True
    False
    True



```python
a = True
if a :
    print("i am inside if")
else :
    print("outside if")
```

    i am inside if



```python
a = False
if a :
    print("inside if")
else :
    print("outside if")
```

    outside if



```python
n = int(input())
if n>0 :
    print("Positive")
elif n<0 :
    print("Negative")
else :
    print("Zero")
```

    20
    Positive



```python
#while loop
n = int(input())
sum = 0
while n>0 :
    sum = sum + n;
    n = n-1
    
print(sum)
```

    10
    55



```python
n = int(input())
i = 0
sum = 0
while (i<=n) :
    if (i%2 == 0):
      sum+=i
    i = i+1

print(sum)
```

    10
    30



```python
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

```

    1
    2
    3
    5



```python
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
```

    121
    true



```python
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

```

    123
    4   2



```python
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

```


```python
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
```

    7
    13


## Patterns problems



```python
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
```

    4
    ****
    ****
    ****
    ****



```python
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
```

    4
    1111
    2222
    3333
    4444



```python
n = int(input())
i = 1
while i <= n :
    j = 1
    while j <= n :
        print(j, end='')
        j = j + 1
    print()
    i = i + 1
```

    4
    1234
    1234
    1234
    1234



```python
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
```

    4
    1
    12
    123
    1234



```python
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
```

    5
    1
    23
    345
    4567
    56789



```python
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
```

    4
    ABCD
    ABCD
    ABCD
    ABCD



```python
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
```

    4
    ABCD
    BCDE
    CDEF
    DEFG



```python
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
```

    5
    *****
    ****
    ***
    **
    *



```python
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
```

    4
       *
      **
     ***
    ****



```python
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
```

    4
       1
      12
     123
    1234



```python
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
```

    5
        1
       121
      12321
     1234321
    123454321



```python
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

```

    5
        *
       ***
      *****
     *******
    *********



```python
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
```

    5
            * 
           * * 
          * * * 
         * * * * 
        * * * * * 
       * * * * * * 
        * * * * * 
         * * * * 
          * * * 
           * * 
            * 



```python
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
```

    5
      *
     ***
    *****
     ***
      *


## More On Loops for loop



```python
s = "Rakesh"
for c in s:
    print(c)
```

    R
    a
    k
    e
    s
    h



```python
# range(start,end,strive)
n = int(input())
for i in range(0, n, 1):
    print(i)
```

    5
    0
    1
    2
    3
    4



```python
n = int(input())
for i in range(n+1):
    print(i)
```

    5
    0
    1
    2
    3
    4
    5



```python
n = int(input())
for i in range(1,n+1):
    print(i)
```

    5
    1
    2
    3
    4
    5



```python
# print multiples of 3
a = int(input())
b = int(input())
for i in range(a,b+1,1):
    if i % 3 == 0 :
        print(i)
```

    2
    20
    3
    6
    9
    12
    15
    18



```python
n = int(input())
for i in range(1,n+1,1):
    for s in range(n-i):
        print(" ", end="")
    for j in range(i,2*i,1):
        print(j,end="")
    for j in range(2*i - 2,i-1,-1):
        print(j,end="")
    print()
```

    5
        1
       232
      34543
     4567654
    567898765


## break


```python
i = 1
while(i<=10):
    if(i==5) :
        break
    print(i)
    i = i + 1
```

    1
    2
    3
    4



```python
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

```

    10
    3



```python
# Decimal to Binary

def DecimalToBinary(num): 
      
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2, end = '') 

n = int(input())
DecimalToBinary(n)
```

    2
    10


```python
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
```

    10
    2



```python
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
        
```

    10
    10



```python
# Trailing zeroes in n!
n = int(input())
sum = 0
r = 1
while(r<=5):
    r = n//5
    sum+=r
print(sum)
    
```

    10



```python

```
