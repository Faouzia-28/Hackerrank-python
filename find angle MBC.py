import math
AB=int(input())
BC=int(input())
MBC=str(round(math.degrees(math.atan2(AB,BC))))+u'\xb0'
print(MBC)
