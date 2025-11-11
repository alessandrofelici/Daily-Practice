def sol(input: str):
  lines = input.split('\n')
  output = 0
  for line in lines:
    output += getRibbonLength(line)
  return output

def getRibbonLength(eq: str):
  nums = eq.split(sep="x")
  for i in range(len(nums)):
    nums[i] = int(nums[i])
  
  l, w, h = nums[0], nums[1], nums[2]
  smallestPerim = min(l*2+w*2, w*2+h*2, l*2+h*2)
  vol = l*w*h

  return vol + smallestPerim