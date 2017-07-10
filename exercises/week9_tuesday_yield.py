'''
Write a function primes() to complete the code below.

Notes on the prime(n=100) function:
- Calcuate primes between 1 and 100 
- Can be used as an iterator
- Is there a difference between using return and yield?
  Please explain

- You will need to write 
1) function that loops through numbers and uses isPrime
2) Line of code that calls written function

'''
#Complete this code
#function to calculate prime
def isPrime(n):
   if n == 1:
      return False
   for t in range(2,n):
      if n % t == 0:
         return False
   return True

#Write additional function here

#Write code that calls new function


#####################################
#Solution 1
for n in primes():
   print n,

#function
def primes(n=1):
   while n < 100:
      # yields n instead of returns n
      if isPrime(n): 
      	yield n
      # next call it will increment n by 1
      n += 1


