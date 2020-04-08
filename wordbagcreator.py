#f = open("banglacorpus.txt", 'r')
f = open("hindicorpus.txt", 'r')

l = f.readlines()
lclean = []
for _ in l:
    lclean += _.split()
print(lclean)
