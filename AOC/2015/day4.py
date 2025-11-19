import hashlib
  
def sol(input):
  num = 254575

  hex = hashlib.md5(input.encode()).hexdigest()

  while hex[:6] != '000000':
    num += 1
    s = f'{input}{num}'
    res = hashlib.md5(s.encode())
    hex = res.hexdigest()
  
  return num