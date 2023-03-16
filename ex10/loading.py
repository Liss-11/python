from time import sleep

def ft_progress(lst):
    for i in lst:
        print('\rETA: [{2:.2f}%] [{0}{1}'.format('=' * int(i/10), '' * (10 - int(i/10)), i), end=">]\r")
        yield i

if __name__=='__main__':
    listy = range(1000) 
    ret = 0
    for elem in ft_progress(listy): 
        ret+=(elem+3) %5
        sleep(0.01) 
    print()
    print(ret)