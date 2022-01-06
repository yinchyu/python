import requests
import json
# from gevent import monkey; monkey.patch_all()
# from threading import Thread
from multiprocessing.pool import ThreadPool
def get_picture_url(page):
    print("当前爬取的页面是： ",page)
    respones = requests.get('https://www.douyu.com/gapi/rkc/directory/0_0/{}'.format(page))
    datas = json.loads(respones.text)
    items = datas['data']['rl']
    for item in items:
        if item['c2name']=='颜值':
            img1=requests.get(item['rs1'][:-4])
            img_name='image\\'+str(item['uid'])+'.jpg'
            img_content=img1.content
            with open(img_name,'wb') as f:  
                f.write(img_content)

# def save_picture(item):
#     img1=requests.get(item['rs1'][:-4])
#     img_name=item['uid']+'_1.jpg'
#     img_content=img1.content
#     with open(img_name,'wb') as f:  
#         f.write(img_content)
    # img2=requests.get(item['res16'][:-4])
    # img1_name=item['uid']+'_1.jpg'
# 使用协程的方法对数据进行处理
# def fun(m,n):
#     tasks=list()
#     for i in range(m,n):
#         tasks.append(gevent.spawn(get_picture_url,i))
#     gevent.joinall(tasks)    

if __name__ == '__main__':
    #使用多线程的方法
    # t1=Thread( target=fun, args=(0,100) )
    # t2=Thread( target=fun, args=(100,201))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()



    # 设置一种线程池的读取方法
    pool=ThreadPool(5)
    for i in range(201):
        pool.apply_async(get_picture_url,args=(i,))
    pool.close()
    pool.join()
    # for i in range(201):
    #     get_picture_url(i)

    # 另一种线程池的加载方式
    pool=ThreadPool()
    ThreadPool.map_async(pool,get_picture_url,[i for i in range(201)])
    pool.map(get_picture_url,[i for i in range(201)])
    





    




# print(content.status_code)
# html = etree.HTML(content)
# print(html)
# page_content=content.text
# pattern=r'<div class="LazyLoad is-visible DyImg DyListCover-pic">*<img src="(*.jpg)*'
# find_result=re.findall(pattern,page_content)
# print(find_result.group(1))
