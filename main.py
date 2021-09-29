'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  if n < 2:
    return False

  for i in range(2, n//2 + 1):
    if n % i == 0:
      return False
  return True
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  prod = 1
  for i in range(len(lst)):
    prod *= lst[i]
  return prod
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  if x < 0:
    x *= -1  
  if y < 0:
    y *= -1

  if y == 0:
    return x
  if x == 0:
    return y

  while x != y:
    if x > y:
      x = x - y
    else:
      y = y - x
  return y
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  b = x
  r = y

  while r != 0:
    i = b % r
    b = r
    r = i
  
  if b < 0:
    b *= -1

  return b
  
  
def main():
  # interfata de tip consola aici
  print('Scrie help pentru a vedea lista de comenzi')
  quit = False
  while not quit:
    command = input('$').split()
    if command[0] == 'help':
      print('cmmdc_v1 [nr1] [nr2] - cel mai mic divizor comun varianta 1')
      print('cmmdc_v2 [nr1] [nr2] - cel mai mic divizor comun varianta 2')
      print('product [nr_list]    - produsul numerelor')
      print('is_prime [nr]        - verifica daca numarul este prim')
      print('quit                 - opreste programul')

    if command[0] == 'cmmdc_v1':
      if len(command) < 3:
        print('Numarul de argumenti prea mic')
        continue
      print(get_cmmdc_v1(int(command[1]), int(command[2])))

    if command[0] == 'cmmdc_v2':
      if len(command) < 3:
        print('Numarul de argumenti prea mic')
        continue
      print(get_cmmdc_v2(int(command[1]), int(command[2])))

    if command[0] == 'product':
      for i in range(1, len(command)):
        q = True
        try:
          command[i] = int(command[i])
        except:
          print('Argumentul', command[i], 'trebuie sa fie numar')
          q = False
          break
      if not q:
        continue
      print(get_product(command[1:]))

    if command[0] == 'is_prime':
      for i in range(1, len(command)):
        try:
          command[i] = int(command[i])
          if is_prime(command[i]):
            print(command[i], 'este prim')
          else:
            print(command[i], 'nu este prim')
        except:
          print(command[i], 'nu este numar')

    if command[0] == 'quit':
      quit = True

if __name__ == '__main__':
  main()
