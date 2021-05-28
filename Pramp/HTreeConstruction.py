import math

def drawHTree(x, y, length, depth):
  drawHTreeOne(x, y, length)
    
  if depth > 1:
    depth -= 1
    length = length / math.sqrt(2)

    drawHTree(x + length / 2, y + length / 2, length, depth)
    drawHTree(x + length / 2, y - length / 2, length, depth)
    drawHTree(x - length / 2, y + length / 2, length, depth)
    drawHTree(x - length / 2, y - length / 2, length, depth)
    
def drawHTreeOne(x, y, length):
  drawLine(x + length / 2, y, x - length / 2, y)
  drawLine(x + length / 2, y + length / 2, x + length / 2, y - length / 2)
  drawLine(x - length / 2, y + length / 2, x - length / 2, y - length / 2)
  
def drawLine(x1, y1, x2, y2):
  print(x1, y1, x2, y2)
  
def main():

    drawHTree(0, 0, 10, 2)

main()