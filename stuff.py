import numpy as np
from PIL import Image

def pixellate(im,lnew):
    img=im.load()
    lold,wold=im.size[0],im.size[1]
    wnew=int(round((wold/lold)*lnew,0))
    ratio = wold//wnew
    woffset=round((wold%wnew)/2,0)
    loffset=round((lold%lnew)/2,0)
    outvals=[]
    for i in range(lnew):
        rowpix=[]
        for j in range(wnew):
            toapt=[0,0,0]
            for k in range(j*(ratio),(j*(ratio))+(ratio)): 
                for l in range(i*(ratio),(i*(ratio))+(ratio)):
                    toapt=[toapt[i]+img[l+loffset,k+woffset][i] for i in range(3)]
            rowpix.append(tuple([int(round(toapt[i]/ratio**2,0)) for i in range(3)]))
        outvals.append(rowpix)
    return outvals

def make8bit(vals,noc):
    return [([tuple([round(k*noc/256,0)*(256/noc) for k in j]) for j in i]) for i in vals]
    
image = Image.open('door.jpg')
length=16
pxls=make8bit(pixellate(image,length),32)
pxli = Image.fromarray(np.array(pxls, dtype=np.uint8).swapaxes(0,1))
pxli.save('output.png')