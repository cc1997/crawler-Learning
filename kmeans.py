#encoding=utf-8
from PIL import Image
import math 
import copy
import random

class Pixel(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.child = []         # 保存归属该类的xy值

    def getDistance(self,P):    # 获取距离
        return math.sqrt(((self.x - P.x)**2 +(self.y - P.y)**2))

    @property
    def xy(self):               # 获取xy
        return (self.x,self.y)
    @property
    def minX(self):             # 获取属于该类的最小x值
        return min([i[0] for i in self.child])
    @property
    def maxX(self):
        return max([i[0] for i in self.child])+1
    @property
    def minY(self):
        return min([i[1] for i in self.child])
    @property
    def maxY(self):
        return max([i[1] for i in self.child])+1
    @property
    def shape(self):            # 获取该类方形分布,左上角,右下角
        return (self.minX,self.minY,self.maxX,self.maxY)

# 获取有用像素点
def getPixelArr(img):           
    pixelArr = []
    for x in range(img.size[0]):
            for y in range(img.size[1]):
                rgb = img.getpixel((x,y))
                if rgb == (0,0,0):
                    pixelArr.append(Pixel(x,y))
    return pixelArr

# 对点分类
def divideClass(img,n):
    pixelArr = getPixelArr(img)
    minX = min([i.x for i in pixelArr])
    maxX = max([i.x for i in pixelArr])
    c = (maxX - minX)/n
    y = img.size[1]/2.0
    k = []
    for i in range(n):
        k.append(Pixel(minX+c*(i+0.5),y))
    showk(k)
    for x in range(10):           #进行10轮计算
        print (x)
        for i in pixelArr:
            dis = 1000
            p = k[0]
            for j in k:
                if i.getDistance(j)<dis:
                    dis = i.getDistance(j)
                    p = j
            p.child.append(i.xy)
        if xxx>=7:
            return k
        k = calcK(k)
    return k

def showk(k):
    print ('k:')
    for i in k:
        print (i.xy)

# 重新计算k
def calcK(k):
    arr = []
    for i in k:
        d = reduce(lambda a,b:(a[0]+b[0],a[1]+b[1]),i.child)
        n = len(i.child)
        arr.append(Pixel(d[0]/n,d[1]/n))
    return arr


def main():
    img  = Image.open("C:/fafu/tif2/19.tif").convert('RGB')         # 请添加一张tif格式的图片
    classArr =  divideClass(img,4)                                  # 分类
    c = [(255,0,0),(255,0,255),(0,0,255),(0,0,0),(199,97,20)]       # rgb数组
    for n,i in enumerate(classArr):
        for xy in i.child:
            img.putpixel(xy,c[n%5])
    img.show()

if __name__=="__main__":
    main()
