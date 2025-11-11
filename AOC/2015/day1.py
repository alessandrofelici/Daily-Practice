def sol(input: str):
  count, pos = 0, 1

  for c in input:
    if c == "(":
      count += 1
    else:
      count -= 1
    
    # Part 2
    if count == -1:
      return pos
    
    pos += 1
    
  return count