import os
import binascii
from PIL import Image
import threading
from tqdm import tqdm


empty = threading.Semaphore(value=20)

def getMatrixfrom_bin(filename, width):  #生成灰度图
    with open(filename, 'rb') as f:
        content = f.read()
    hexst = binascii.hexlify(content)  #将二进制文件转换为十六进制字符串
    fh = numpy.array(
        [int(hexst[i:i + 2], 16) for i in range(0, len(hexst), 2)])  #按字节分割
    rn = int(len(fh) / width)
    fh = numpy.reshape(fh[:rn * width], (-1, width))  #根据设定的宽度生成矩阵
    fh = numpy.uint8(fh)
    return fh

def generate_gray(fp):
    filename = fp
    try:
        im = Image.fromarray(getMatrixfrom_bin(filename, 512))  #转换为图像
        im = im.resize((512, 512))
        PNG = filename + '.png'
        im.save(PNG)
    except Exception as e:
        pass
    os.remove(fp)

    empty.release()
    

real_path = []
with tqdm(total=len(real_path[6007:]), ncols=80, desc="gray") as pbar:
    for fp in real_path[6007:]:
        empty.acquire()
        t = threading.Thread(target=generate_gray, args=(fp, ), daemon=True)
        t.start()
        pbar.update(1)
