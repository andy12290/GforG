# list comphrehension

lst = [row ** 2 for row in range(1,11) if row % 2 == 1]
print(lst)

# power of 2
power_2 = [ 2 **i for i in range(1,8) ]
print(power_2)

# Non primes number
non_primes = [ y for x in range(2,8) for y in range(x*2, 50, x)]
print(non_primes)
