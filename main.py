MAX = 100

sum_even = 0
sum_odd = 0
for i in range(1, MAX+1):
  if i % 2 == 0: sum_even += i
  else: sum_odd += i
print(f'Suma parzystych {sum_even}\nSuma nieparzystych {sum_odd}')
