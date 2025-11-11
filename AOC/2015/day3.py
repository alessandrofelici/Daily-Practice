


def sol(directions: str):
  dict = {
    (0,0): 1
  }
  loc = (0,0)

  for c in directions:
    if c == "^":
      loc = (loc[0], loc[1] + 1)
    elif c == ">":
      loc = (loc[0] + 1, loc[1])
    elif c == "v":
      loc = (loc[0], loc[1] - 1)
    else:
      loc = (loc[0] - 1, loc[1])

    if loc in dict:
      dict[loc] += 1
    else:
      dict[loc] = 1

  frequentlyVisited = 0
  for value in dict.values():
    if value > 0:
      frequentlyVisited += 1

  return frequentlyVisited
    