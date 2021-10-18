import multiprocessing

from proc_ebook import proccess_ebook

def worker(filename):
    """thread worker function"""
    result = proccess_ebook(filename)
    print(result)
    
if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=('pg36099.txt',))
    p2 = multiprocessing.Process(target=worker, args=('pg66474.txt',))
    p.start()
    p2.start()
