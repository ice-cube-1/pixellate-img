import numpy as np
from PIL import Image
def pixellate(im,lnew,noc=256,contrast=False):
    lold,wold,img=im.size[0],im.size[1],im.load()
    wnew=int(round((wold/lold)*lnew,0))
    ratio = wold//wnew
    woffset,loffset=(wold%wnew)//2,(lold%lnew)//2
    usualc = [[[round(sum(img[k,l][m] for k in range(i*ratio+loffset,i*ratio+ratio+loffset) for l in range(j*ratio+woffset,j*ratio+ratio+woffset))//(ratio**2)*(noc/256),0)*256/noc for m in range(3)] for j in range(wnew)] for i in range(lnew)]
    if contrast:
        for i in range(lnew):
            for j in range(wnew):
                for k in range(3):
                    x=0
                    if i > 0: x += 1 if usualc[i][j][k] > usualc[i-1][j][k] else -1
                    if i < lnew-1: x += 1 if usualc[i][j][k] > usualc[i+1][j][k] else -1
                    if j > 0: x += 1 if usualc[i][j][k] > usualc[i][j-1][k] else -1
                    if j < wnew-1: x += 1 if usualc[i][j][k] > usualc[i][j-1][k] else -1
                    usualc[i][j][k]+=x*noc//contrast
    return [[tuple(l) for l in m] for m in usualc]
Image.fromarray(np.array(pixellate(Image.open('files/cat.jpg'),32,32,32), dtype=np.uint8).swapaxes(0,1)).save('output.png')