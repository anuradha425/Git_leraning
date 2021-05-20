""
##**********************Sum of natural numbers******************************
def natural_number(num):
    if num < 0:
        print("Enter a positive number")
    else:
        sum = 0
        # use while loop to iterate un till zero
        while (num > 0):
            sum += num
            num -= 1
        print("The sum is", sum)
print(natural_number(20))

#********************Arm srtong number for intervals*************************
def armstrong_intervals(lower, upper):
    l=[]
    for num in range(lower, upper + 1):
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
            if num == sum:
                print(num)
                l.append(num)
    print(l)
print(armstrong_intervals(100,500))

#*************************Armstrong number*************************************
def arm_strong(num):
    sum = 0
    tmp = num
    while tmp>0:
        digit = tmp%10
        sum = sum + digit**3
        tmp = tmp//10
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
print(arm_strong(147))

#*************************fibnoci series ****************************************
def fib(num):
    count = 0
    n1,n2 = 0,1
    while count < num:
        print(n1)
        n1,n2 = n2, n1 + n2
        count = count + 1

print(fib(8))

def F():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

F()

###***************************Multiplication of table is ************************
def mul_table(num):
    for i in range(1,11):
        print("Result is  ",num,'x',i,'=',num*i)
print(mul_table(10))

################# find a factorial of given number ####################################
def facto(num):
    if num < 0:
        print("Negative numbers not have factorial")
    elif num == 0:
        print("o number factorial is always 1")
    else:
        factorial =1
        for i in range(1,num +1):
            factorial = factorial * i
        print(num,"factorial value is ", factorial)
print(facto(5))

################ prime numbers between intervals like 10 and 50 #################################
def prime_interval(lower,upper):
    prime_list= []
    for num in range(lower, upper + 1):
        if num>1:
            for i in range(2,num):
                if num%i == 0:
                    break
            else:
                print(num)
                prime_list.append(num)
    print(prime_list)
print(prime_interval(1,20))

################write a program to find the given number is prime or not ################################

def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")
print(check_prime(105))

###### Find gcd of more than two numbers ######################

def find_gcd(x,y):
    while y:
        x,y = y, x%y
    return x
#print(find_gcd(10,150))
l =[50,40,100]
n1 =l[0]
n2= l[1]
gcd = find_gcd(n1,n2)
for i in range(2,len(l)):
    gcd= find_gcd(gcd,l[i])
print(gcd)

############ find gcd or hcf without using builtin functions #################

def f(x,y):
    while(y):
        x,y = y, x%y
    return x
print(f(100,150))


#########finnd second largest number in a list without using any builtin function#######
l = [10,20,30,50,40]
largest = second_largest = -10000
for x in l:
    if x>largest:
        tmp = largest
        largest = x
        second_largest = tmp
    elif x > second_largest and x!= largest:
        second_largest = x
print(second_largest,largest)


##########find second smallest nnumber in a list without using builtin function##########

l = [10,20,30,50,40]
smalest = second_smalest = 9999
for x in l:
    if x< smalest:
        tmp = smalest
        smalest = x
        second_smalest = tmp
    elif x < second_smalest and x!= smalest:
        second_smalest = x
print(second_smalest,smalest)

########largest number without using any builtin function###################

largest = -10000
for x in l:
    if x>largest:
        tmp = largest
        largest = x
print(largest)
##########smallest number without using any builtin function#################
smallest = 99999
for x in l:
    if x < smallest:
        tmp = smallest
        smallest = x
print(smallest)
###########count repeted elements in a list without using builtin functions####
d = {}
for x in l:
    if x in d:
        d[x] = d[x]+1
    else:
        d[x]=1
print(d)
"""
