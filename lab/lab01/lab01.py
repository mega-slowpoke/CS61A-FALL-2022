def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1                           
    i = 1                      # 计数，已经乘了的数的个数        
    while i <= k:              # k是总共要乘的数的个数
        result = result * n                 
        n -= 1                           
        i += 1                           
    return result
    
    # result = 1    
    # stop = n - k   (停下的数字，在上面的例子中就分别是4,2,4,/)
    # while n > stop:
    #     result = result * n 
    #     n -= 1
    # return result

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    result = 0 
    for i in str(y):      #str(y)转化为字符串，循环表示将字符串逐位输出
        result += int(i)  #逐位输出的是字符串格式，要转化为int才能相加
    return result

    # 标准答案的解法是反过来想的，从个位加到10位
    # result = 0
    # while y > 0:         
    #     result += y % 10   #除以10的余数就是个位
    #     y = y // 10        #除以10向下取整就删掉一位数了
    # return result
    


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    #字符串解法
    n = str(n)
    if "88" in n:
        return True
    else:
        return False

    #代数解法，就和上题差不多
    # prev_digit = n % 10                         #先求出上一位（最后一位）
    # n = n // 10
    # current_digit = n % 10                      #再求出当前位（倒数第二位）
    # while n > 0:                                #如果此时n还有位数，继续循环
    #     if current_digit == prev_digit == 8:    #
    #         return True
    #     else:
    #         prev_digit = current_digit          #当前位变上一位
    #         n = n // 10              
    #         current_digit = n % 10              #往前推，求出新的当前位
    # return False


def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    #  字符串解法
    #  number_list = []
    #  for i in str(n):
    #      number_list.append(i)
    #  number_set = set(number_list)
    #  return len(number_set)

    #代数解法，需要定义两个函数
    total = 0                    #unique_digits的个数
    for i in range(0,10):        #遍历0-9，看n里面包含哪些数
        if has_digit(n,i):
            total += 1           #如果包含该数，unique_digits + 1
    return total

def has_digit(n, k):                        
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"
    while n > 0:                    #和之前的原理一样，用%和//来切割位数
        current_digit = n % 10 
        if current_digit == k:
            return True
        n = n // 10
    return False

    
    

