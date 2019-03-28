#coding:utf-8



# 电影院当前座位排数
def test2(n):
    """想知道自己的座位是电影院的第几排，可以问前一排，前一排的可以继续问前一排，直到第一排知道自己是第一排"""
    if n==1:return 1
    return test2(n-1)+1


# 全局变量，表示递归的深度
DEPTH=0 

# 电影院当前座位排数
def test3(n):
    """想知道自己的座位是电影院的第几排，可以问前一排，前一排的可以继续问前一排，直到第一排知道自己是第一排"""
    global DEPTH    
    if DEPTH>10:
        raise ValueError('递归深度错误')
    DEPTH+=1    

    if n==1:return 1
    return test3(n-1)+1

# 求解台阶走法
def test1(n):
    """一个台阶可以一次走一个台阶，也可以一次走两个台阶，求台阶有多少种走法"""
    if n==1:return 1
    if n==2:return 2
    return test1(n-1)+test1(n-2)


# 利用dict 形成一个 map，key 是 n ,value 是 f(n)
MAP_DICT={}

# 求解台阶走法
def test4(n):
    """一个台阶可以一次走一个台阶，也可以一次走两个台阶，求台阶有多少种走法"""
    if n==1:return 1
    if n==2:return 2
    
    if MAP_DICT.get(n):
        return MAP_DICT.get(n)
    ret = test4(n-1)+test4(n-2)
    MAP_DICT[n]=ret
    return ret

# 电影院非递归
def test5(n):
    ret=1
    for i in range(2,n+1):
        ret+=1
    return ret

# 台阶非递归
def test6(n):
    if n==1:return 1
    if n==2:return 2
    ret=1
    pre=2
    prepre=1
    for i in range(3,n+1):
        ret=pre+prepre
        prepre=pre
        pre=ret
    return ret



def main():
    print(test6(7))

if __name__ == '__main__':
    main()