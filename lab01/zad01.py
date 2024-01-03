def prime(n):
  counter = 0
  for i in range(1, n+1):
    if n % i == 0:
      counter += 1
  if counter == 2:
    return True
  return False

print(prime(3))

def select_primes(n):
  result = []
  for i in n:
    if prime(i):
      result.append(i)
  return result

print(select_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))