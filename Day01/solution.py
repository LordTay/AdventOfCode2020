#Solution of Day1

target = 2020

file_path = "./input1"

try:
    f = open(file_path,"r")
except Exception as e:
    print("Exception: ",e)

l = []
d = {}
for i in f:
    d[int(i)]=i
    l.append(int(i))
l.sort()


for i in l:
    if (target-i) in d:
        print("a = ",i,", b = ",(target-i))
        print("solution = ", i*(target-i))
        break