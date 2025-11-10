import importlib.util
import fileinput

# Define module name and file path
path = "D:/GitHub/Daily-Practice/AOC/2015/day1.py"
mname = "mod"

# Load module from specified file location
spec = importlib.util.spec_from_file_location(mname, path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

# file input
filename = "D:/GitHub/Daily-Practice/AOC/util/input.txt"

output = ""
for line in fileinput.input(files=filename):
  output += str(mod.day1(line))

with open("AOC/util/output.txt", "w") as f:
  f.write(output)