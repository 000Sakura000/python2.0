#6
#6
import math
AB=eval(input())
CD=eval(input())
AD=AB/2
OA=(AD**2+CD**2)/(2*CD)
r=OA
AOB=2*math.asin(AD/OA)
sector = AOB / (2*math.pi) * math.pi *OA**2
triangle = 1 / 2 * OA**2 * math.sin(AOB)
arch = sector - triangle
print(f"{arch:.2f}")
