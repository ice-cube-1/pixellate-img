import numpy as np
from PIL import Image

def pixellate(im,lnew):
    img=im.load()
    lold,wold=im.size[0],im.size[1]
    wnew=int(round((wold/lold)*lnew,0))
    ratio = wold//wnew
    woffset=int(round((wold%wnew)/2,0))
    loffset=int(round((lold%lnew)/2,0))
    return [[tuple([sum(img[k,l][m] for k in range(i*ratio+loffset,i*ratio+ratio+loffset) for l in range(j*ratio+woffset,j*ratio+ratio+woffset))//(ratio**2) for m in range(3)]) for j in range(wnew)] for i in range(lnew)]

def make8bit(vals,noc):
    return [([tuple([round(k*noc/256,0)*(256/noc) for k in j]) for j in i]) for i in vals]
    
image = Image.open('door.jpg')
length=16
pxls=make8bit(pixellate(image,length),32)
pxli = Image.fromarray(np.array(pxls, dtype=np.uint8).swapaxes(0,1))
pxli.save('output.png')