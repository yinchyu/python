def isRayIntersectsSegment(poi,s_poi,e_poi): #[x,y] [lng,lat]
    #输入：判断点，边起点，边终点，都是[lng,lat]格式数组
    if s_poi[1]==e_poi[1]: #排除与射线平行、重合，线段首尾端点重合的情况
        return False
    if s_poi[1]>poi[1] and e_poi[1]>poi[1]: #线段在射线上边
        return False
    if s_poi[1]<poi[1] and e_poi[1]<poi[1]: #线段在射线下边
        return False
    if s_poi[1]==poi[1] and e_poi[1]>poi[1]: #交点为下端点，对应spoint
        return False
    if e_poi[1]==poi[1] and s_poi[1]>poi[1]: #交点为下端点，对应epoint
        return False
    if s_poi[0]<poi[0] and e_poi[1]<poi[1]: #线段在射线左边
        return False

    xseg=e_poi[0]-(e_poi[0]-s_poi[0])*(e_poi[1]-poi[1])/(e_poi[1]-s_poi[1]) #求交
    if xseg<poi[0]: #交点在射线起点的左侧
        return False
    return True  #排除上述情况之后
def isPoiWithinPoly(poi,poly):
    #输入：点，多边形三维数组
    #poly=[[[x1,y1],[x2,y2],……,[xn,yn],[x1,y1]],[[w1,t1],……[wk,tk]]] 三维数组

    #可以先判断点是否在外包矩形内 
    #if not isPoiWithinBox(poi,mbr=[[0,0],[180,90]]): return False
    #但算最小外包矩形本身需要循环边，会造成开销，本处略去
    sinsc=0 #交点个数
    for epoly in poly: #循环每条边的曲线->each polygon 是二维数组[[x1,y1],…[xn,yn]]
        for i in range(len(epoly)-1): #[0,len-1]
            s_poi=epoly[i]
            e_poi=epoly[i+1]
            if isRayIntersectsSegment(poi,s_poi,e_poi):
                sinsc+=1 #有交点就加1

    return True if sinsc%2==1 else  False

import json
import csv
def pointInPolygon():
    gfile = './beijing_poly_wgs84.geojson' #utf-8编码
    cin_path = './poi_cinema_wgs84.csv'
    out_path = './beijing_poi_cinema_wgs84.csv' #输出文件

    pindex = [2, 3]  # wgslng,wgslat 在的位置

    with open(out_path, 'w', newline='') as cout_file:
        fin = open(cin_path, 'r', encoding='gbk') #出现编码错误就改编码 utf-8
        gfn = open(gfile, 'r', encoding='utf-8')
        gjson = json.load(gfn)
        polygon = gjson["features"][0]["geometry"]['coordinates'] #提取多边形,如果是4维数组需要相应的处理
        filewriter = csv.writer(cout_file, delimiter=',')
        w = 0
        for line in csv.reader(fin, delimiter=','):
            if w == 0: #写入表头 id,name,… 如果没有就去掉if语句
                filewriter.writerow(line)
                w = 1
                continue
            point = [float(line[pindex[0]]), float(line[pindex][1])]
            if isPoiWithinPoly(point, polygon): #在多边形内，写入新表
                filewriter.writerow(line)
            else:
                continue
        fin.close()
        gfn.close()
    print('done')
