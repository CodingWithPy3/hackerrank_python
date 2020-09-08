from cmath import phase
ip = complex(input())

r = ((ip.real**2)+ (ip.imag**2) )**0.5
angle = phase(ip)
print(r)
print(angle)
