'''
Author:yiqunzhao
E-mail:13456591503@163.com
'''
import numpy as np

########################################################################################################################
####校园平面图#####
index= {'0':'丁香餐厅','1':'竹园餐厅','2':'海棠餐厅','3':'北操场',
        '4':'南操场','5':'工训中心','6':'图书馆','7':'体育馆',
        '8':'东门','9':'北门','10':'校医院','11':'大活'}
introduce= {'丁香餐厅':'丁香餐厅位于丁香公寓附近，供住在丁香公寓的学生及教职工用餐之用',
            '竹园餐厅':'竹园餐厅位于竹园公寓附近，供住在竹园公寓的学生及教职工用餐之用',
            '海棠餐厅':'海棠餐厅位于海棠公寓附近，供住在海棠公寓的学生及教职工用餐之用',
            '北操场':'北操场位于学校西北角，设有足球场和主席台，可以举行运动会',
            '南操场':'南操场位于学校西南角，设有足球场等设施',
            '工训中心':'工训中心位于学校中间位置，负责学生金工实习的教学实践任务',
            '图书馆':'图书馆位于E楼旁，供学生借阅图书及自习之用',
            '体育馆':'远望谷体育馆新建于2017年，位于学校东南面',
            '东门':'东门位于西沣路上，是学校主要的主要出口之一',
            '北门':'北门位于学校北面，是学校主要的主要出口之一',
            '校医院':'校医院位于学校东北角上，时刻关注学生健康问题',
            '大活':'大学生活动中心位于学校西面，为学生组织活动提供场所'}
map=np.array([  [0   ,0   ,0   ,0   ,293 ,0   ,291 ,840 ,0   ,0   ,0   ,0   ],
                [0   ,0   ,584 ,0   ,0   ,169 ,0   ,0   ,0   ,330 ,237 ,0   ],
                [0   ,584 ,0   ,319 ,0   ,543 ,0   ,0   ,0   ,328 ,0   ,0   ],
                [0   ,0   ,319 ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,416 ],
                [293 ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,203 ],
                [0   ,169 ,543 ,0   ,0   ,0   ,430 ,0   ,458 ,0   ,0   ,0   ],
                [291 ,0   ,0   ,0   ,0   ,430 ,0   ,0   ,0   ,0   ,0   ,484 ],
                [840 ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,243 ,0   ,0   ,0   ],
                [0   ,0   ,0   ,0   ,0   ,458 ,0   ,243 ,0   ,0   ,502 ,0   ],
                [0   ,330 ,328 ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
                [0   ,237 ,0   ,0   ,0   ,0   ,0   ,0   ,502 ,0   ,0   ,0   ],
                [0   ,0   ,0   ,416 ,203 ,0   ,484 ,0   ,0   ,0   ,0   ,0   ]])
########################################################################################################################

def introduction():
    '''
    介绍12个景点之用,实现介绍景点的功能
    '''

    print('\n\n目前地图拥有12个景点:\n0:丁香餐厅,1:竹园餐厅,2:海棠餐厅,3:北操场\n4:南操场,  5:工训中心,6:图书馆,  7:体育馆\n8:东门,    9:北门,    10:校医院, 11:大活')
    place=input('请选择您想要了解的景点:')
    list=['0','1','2','3','4','5','6','7','8','9','10','11']
    while place not in list:
        print('您选择的景点不在地图范围内！')
        place=input('请选择您想要了解的景点:')
    print(introduce[index[place]])

def distance(i,j):
    '''
    考虑到各个点之间的实际距离比较难以测量，故在地图上通过测量两点间直线距离代替，返回的是(i,j)间的距离
    '''

    if i<12 and j<12 and i>=0 and j>=0:
        return(map[i][j])
    else:
        print('对不起，景点不在地图范围内！')
        return(0)

def shortest_path(i,j):
    '''
    通过Dijkstra算法求最短路径问题，返回的是一个包含关键点的列表
    '''

    X=[i]   #已确定距离的点
    Y=[0,1,2,3,4,5,6,7,8,9,10,11]   #未确定距离的点
    route_x=[[i,i,0]]   #起到类似邻接表的作用
    Y.remove(i) #去掉起点

    #找出最短路径
    while j not in X:
        mini_dist=1000000000
        present_point=j
        next_point=j
        for p1 in route_x:
            for p2 in Y:
                if distance(p1[1],p2)!=0 and p1[2]+distance(p1[1],p2)<=mini_dist:
                    mini_dist=p1[2]+distance(p1[1],p2)
                    present_point=p1[1]
                    next_point=p2
        X.append(next_point)
        route_x.append([present_point,next_point,mini_dist])
        Y.remove(next_point)
    # print(route_x)

    #整理出最短路径的线路
    final_distance=route_x[-1][2]
    final_point=route_x[-1][1]
    last_point=route_x[-1][0]
    the_route=[final_point,last_point]
    while last_point!=i:
        for R in route_x:
            if R[1]==last_point:
                last_point=R[0]
                the_route.append(last_point)
    the_route.reverse()
    print(the_route)

    return the_route

def navigation():
    '''
    实现导航，即问路查询功能
    '''
    print('\n\n目前地图拥有12个景点:\n0:丁香餐厅,1:竹园餐厅,2:海棠餐厅,3:北操场\n4:南操场,  5:工训中心,6:图书馆,  7:体育馆\n8:东门,    9:北门,    10:校医院, 11:大活')
    start = int(input('请选择起点:'))
    while start not in range(12):
        start = int(input('起点不在地图范围内，请重新选择:'))
    end = int(input('请选择终点:'))
    while end not in range(12):
        end = int(input('终点不在地图范围内，请重新选择:'))
    if start == end:
        print('终点就在起点处！')
    else:
        path=shortest_path(start, end)
        for i in range(len(path)-1):
            print(index[str(path[i])]+'---->'+index[str(path[i+1])])

def interface_chn():
    '''
    交互界面，该版本采用中文交互，实现功能的选择和退出程序的功能
    '''

    print('欢迎使用西电校园导航系统 !')
    print('本系统有如下功能:\n1)介绍学校景点;\n2)为您导航;\n3)退出;')
    choose=int(input('请选择您想要的功能 (1/2/3):'))
    while True:
        while choose not in [1,2,3]:
            choose = int(input('对不起，您的选择超出了范围，请重新选择(1/2/3):'))
        if choose==1:
            introduction()
        elif choose==2:
            navigation()
        elif choose==3:
            print('已结束程序，谢谢您的使用，再见！')
            break
        print('\n\n本系统有如下功能:\n1)介绍学校景点;\n2)为您导航;\n3)退出;')
        choose = int(input('请选择您想要的功能 (1/2/3):'))

########################################################################################################################
if __name__=='__main__':
    interface_chn()
