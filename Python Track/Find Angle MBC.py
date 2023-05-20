import math
AB = int(input())
BC = int(input())
angle = (math.atan(AB/BC))
angle2 = round(math.degrees(angle))
print(angle2,chr(176),sep='')
