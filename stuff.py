import numpy as np
from PIL import Image

def pixellate(im,lnew):
    img=im.load()
    lold=im.size[0]
    wold=im.size[1]
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

image = Image.open('candle.jpeg')
length=16
pxls=pixellate(image,length)
pxli = Image.fromarray(np.array(pxls, dtype=np.uint8).swapaxes(0,1))
pxli.save('output.png')