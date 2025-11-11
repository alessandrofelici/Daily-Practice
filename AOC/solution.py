import importlib.util

# ***** CHANGE ME *****
path = "D:/GitHub/Daily-Practice/AOC/2015/day3.py"
mname = "mod"

# Load module from specified file location
spec = importlib.util.spec_from_file_location(mname, path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

# ***** CHANGE ME *****
testing = False
inputFile = 'test.txt' if testing else 'input.txt' 

with open(f'D:/GitHub/Daily-Practice/AOC/{inputFile}', 'r') as f:
    content = f.read()
    output = mod.sol(content)

if testing:
   print(output)

with open("D:/GitHub/Daily-Practice/AOC/output.txt", "w") as f:
  if type(output) == "string":
    f.write(output)
  else:
    f.write(str(output))
