import numpy as np
from PIL import Image

length = 64
im = Image.open('idkthing.png')
l=im.load()
sizeorig=im.size[0]
lsmallrow=[]
for i in range(length):
    toaplsr=[]
    for j in range(length):
        toaptr,toaptg,toaptb=0,0,0
        for k in range(j*(sizeorig//length),(j*(sizeorig//length))+(sizeorig//length)):
            for m in range(i*(sizeorig//length),(i*(sizeorig//length))+(sizeorig//length)):
                toaptr+=l[m,k][0]
                toaptg+=l[m,k][1]
                toaptb+=l[m,k][2]
        toaptr=int(round(toaptr/(sizeorig//length)**2,0))       
        toaptg=int(round(toaptg/(sizeorig//length)**2,0))
        toaptb=int(round(toaptb/(sizeorig//length)**2,0))
        toaplsr.append((toaptr,toaptg,toaptb))
    lsmallrow.append(toaplsr)
array = np.array(lsmallrow, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image = new_image.rotate(-90)
new_image.save('img.png')