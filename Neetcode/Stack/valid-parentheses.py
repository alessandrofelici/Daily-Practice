

def isValid(s: str) -> bool:
  stack = []
  openToClose = {
    "{" : "}",
    "[" : "]",
    "(" : ")"
  }
  for c in s:
    # 
    if s.find(openToClose(c)) != -1:
      
      # other half not in string
        # was removed already
        # doesnt exist

    # other half is in string



print(isValid("{[]}"))

