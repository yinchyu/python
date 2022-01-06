import os
from multiprocessing.queues import Queue
from multiprocessing import Pool,Manager,freeze_support
import time
import tqdm


# 对文件进行写操作
def write_file(q,old_file_path,new_file_path,i):
    with open(os.path.join(old_file_path,i),'r') as old_f:
            with open(os.path.join(new_file_path,i),'a+') as new_f:
                 for f in old_f.readlines():
                     new_f.writelines(f)
            # print('write {} done'.format(i))
            q.put(i)

def write_file_for(old_file_path,new_file_path,i):
    with open(os.path.join(old_file_path,i),'r') as old_f:
            with open(os.path.join(new_file_path,i),'a+') as new_f:
                 for f in old_f.readlines():
                     new_f.writelines(f)
            # print('write {} done'.format(i))
            

        
def main():
    # 先读取文件位置， 然后读取文件个数
    #创建新的文件夹， 然后读入一个文件就加入进程池， 然后让进程池完成操作
    old_file_path=r'C:\Users\11928\Desktop\2020杂项\录音\YCY'
    new_file_path=r'C:\Users\11928\Desktop\2020杂项\录音\YCY副本'
    try:

        os.mkdir(new_file_path)
    except:
        pass
    #初始化进程池
    po=Pool(3)
    # 传入读取的文件， 然后用多个文件进行写操作
    file_list=os.listdir(old_file_path)
    file_list_len=len(file_list)
    file_check=list()
    q=Manager().Queue()


    print('-----------进程池----------')
    start_time=time.time()
    for i in file_list:
        # write_file(old_file_path,new_file_path,i)
        # 只用提交到池子对应的任务即可
        po.apply_async(write_file,args=(q,old_file_path,new_file_path,i))
    po.close()
    # po.join()
    copy_name=0.0
    while True:
        filename=q.get()
        copy_name+=1.0
        bili=(copy_name/file_list_len*1.0)#计算完成和总共的比例
        print('\r现在完成进度是{:.2%}'.format(bili),end='')
        if copy_name>=file_list_len:
            break
        
    stop_time=time.time()
    print()
    print('使用线程池用时：{:.5f}s'.format(stop_time-start_time))




    print('-----------for循环----------')
    start_time=time.time()
    for i in tqdm.tqdm(file_list):
        write_file_for(old_file_path,new_file_path,i)
    stop_time=time.time()
    print('使用正常的for循环用时：{:.5f}s'.format(stop_time-start_time))



if __name__ == '__main__':
    freeze_support()
    main()