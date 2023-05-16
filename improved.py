import numpy as np
from PIL import Image
im = Image.open('idkthing.png')
l=im.load()
origl=im.size[0]
origw=im.size[1]
lgth=32
w=int(round((origw/origl)*lgth,0))
print(w,lgth)
lsmallrow=[]
for i in range(lgth):#
    toaplsr=[]
    for j in range(w):
        toaptr,toaptg,toaptb=0,0,0
        for k in range(j*(origw//w),(j*(origw//w))+(origw//w)):
            for m in range(i*(origl//lgth),(i*(origl//lgth))+(origl//lgth)):
                toaptr+=l[m,k][0]
                toaptg+=l[m,k][1]
                toaptb+=l[m,k][2]
        toaptr=int(round(toaptr/(origl*origw/(lgth*w)),0))       
        toaptg=int(round(toaptg/(origl*origw/(lgth*w)),0))
        toaptb=int(round(toaptb/(origl*origw/(lgth*w)),0))
        toaplsr.append((toaptr,toaptg,toaptb))
    lsmallrow.append(toaplsr)
array = np.array(lsmallrow, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image = new_image.rotate(-90)
new_image.save('img.png')