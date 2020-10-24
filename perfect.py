n = int(input()) 

def perfect_number(n):
    dividers = [i for i in range(1,n) if n%i==0]
    sum_dividers = 0

    for i in dividers:
        sum_dividers +=i
        
    if sum_dividers == n:
         return "It's a perfect number"
    else: 
        return "It's not a perfect number"

print(perfect_number(n))