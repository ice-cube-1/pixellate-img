import numpy as np
from PIL import Image
im = Image.open('candle.jpeg')
l=im.load()
origl=im.size[0]
origw=im.size[1]
lgth=16
w=int(round((origw/origl)*lgth,0))
ratio = origw//w
woffset=round((origw%w)/2,0)
loffset=round((origl%lgth)/2,0)
lsmallrow=[]
for i in range(lgth):
    toaplsr=[]
    for j in range(w):
        toapt=[0,0,0]
        for k in range(j*(ratio),(j*(ratio))+(ratio)):
            for m in range(i*(ratio),(i*(ratio))+(ratio)):
                toapt=[toapt[i]+l[m+loffset,k+woffset][i] for i in range(3)]
        toaplsr.append(tuple([int(round(toapt[i]/ratio**2,0)) for i in range(3)]))
    lsmallrow.append(toaplsr)
array = np.array(lsmallrow, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image = new_image.rotate(-90)
new_image = new_image.transpose(Image.FLIP_LEFT_RIGHT)
new_image.save('img.png')