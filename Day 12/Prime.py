def is_prime(num):
    
    for n in range(2, num) :
        
        if num % n == 0 :
            return False
    return True

print(is_prime(int(input("Give the no. to check for prime :"))))


# A basic code to check if a no. is prime or not using brute approach.