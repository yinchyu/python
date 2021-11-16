from multiprocessing import Process
from multiprocessing import shared_memory

share_nums = shared_memory.ShareableList(range(5))

def work1(nums):
    for i in range(5):
        nums[i] += 10
    print(f'work1 {nums= }')

def work2(nums):
    print(f'work2 {nums= }')

if __name__ == '__main__':
    p1 = Process(target=work1, args=(share_nums, ))
    p1.start()
    p1.join()
    p2 = Process(target=work2, args=(share_nums, ))
    p2.start()

# work1 nums= ShareableList([10, 11, 12, 13, 14], name='wnsm_b5d3682b')
# work2 nums= ShareableList([10, 11, 12, 13, 14], name='wnsm_b5d3682b')
#  测试的3.8中的特性
