


def sol(directions: str):
  dict = {
    (0,0): 2
  }
  loc1 = (0,0)
  loc2 = (0,0)

  count = 0
  for c in directions:
    loc_temp = loc1 if count % 2 == 0 else loc2
    
    if c == "^":
      loc_temp = (loc_temp[0], loc_temp[1] + 1)
    elif c == ">":
      loc_temp = (loc_temp[0] + 1, loc_temp[1])
    elif c == "v":
      loc_temp = (loc_temp[0], loc_temp[1] - 1)
    else:
      loc_temp = (loc_temp[0] - 1, loc_temp[1])

    if loc_temp in dict:
      dict[loc_temp] += 1
    else:
      dict[loc_temp] = 1
    
    if count % 2 == 0:
      loc1 = loc_temp
    else:
      loc2 = loc_temp
    count += 1


  frequentlyVisited = 0
  for value in dict.values():
    if value > 0:
      frequentlyVisited += 1

  return frequentlyVisited
    