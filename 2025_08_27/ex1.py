V = [2,6,8,3,10,9,1,21,33,14]

X = 2
Y = 4

print(V[X+1]) #V[3]
print(V[X+2]) #V[4]
print(V[X+3]) #V[5]
print(V[X*4]) #V[8]
print(V[X*1])
print(V[X*2])
print(V[X*3])
print(V[V[X+Y]]) #V[6]
print(V[X+Y])
print(V[8-V[2]]) # V[8 - 8]   V[0]
#print(V[V[4]])   # V[10]   out of range  [0..9]
print(V[V[V[7]]])  #V[V[21]]   index out of bounds
print(V[V[1]*V[4]])  #V[4 * 10]  V[40]
print(V[X+4]) 