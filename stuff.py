import numpy as np
from PIL import Image
def pixellate(im,lnew,noc=256):
    lold,wold,img=im.size[0],im.size[1],im.load()
    wnew=int(round((wold/lold)*lnew,0))
    ratio = wold//wnew
    woffset,loffset=int(round((wold%wnew)/2,0)),int(round((lold%lnew)/2,0))
    return [[tuple([round(sum(img[k,l][m] for k in range(i*ratio+loffset,i*ratio+ratio+loffset) for l in range(j*ratio+woffset,j*ratio+ratio+woffset))//(ratio**2)*(noc/256),0)*256/noc for m in range(3)]) for j in range(wnew)] for i in range(lnew)]
Image.fromarray(np.array(pixellate(Image.open('door.jpg'),16,32), dtype=np.uint8).swapaxes(0,1)).save('output.png')