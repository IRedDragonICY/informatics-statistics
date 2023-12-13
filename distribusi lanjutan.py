# mencari distribusi normal
import math
# scipy
from scipy.stats import norm
x = 778
std = 40
u = 800

# distribusi normal = 1/2(1 + erf((x-u)/std*sqrt(2)))


z1 = 1/(math.sqrt(2*math.pi)*std) * math.exp(-1/2 * ((x-u)/std)**2)
# dengan step by step
print("n(x;u,std) = 1/(std*sqrt(2*pi)) * exp(-1/2 * ((x-u)/std)**2)")
print("n({};{};{}) = 1/({}*sqrt(2*pi)) * exp(-1/2 * (({}-{})/{})**2)".format(x,u,std,std,x,u,std))
print(z1)

# dengan x = 834
x = 834
z2 = 1/(math.sqrt(2*math.pi)*std) * math.exp(-1/2 * ((x-u)/std)**2)
print("n({};{};{}) = 1/({}*sqrt(2*pi)) * exp(-1/2 * (({}-{})/{})**2)".format(x,u,std,std,x,u,std))
print(z2)
# CARI PERBEDAAN
print(math.fabs(z1-z2))

# dengan scipy
print("dengan scipy")
x = 778
z3= norm.pdf(x,u,std)
print(z3)
x = 834
result4 = norm.pdf(x,u,std)
# selisih

print(math.fabs(result4-result3))
