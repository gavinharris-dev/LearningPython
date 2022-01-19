
def colitz(num):
    print(num)
    
    while num != 1:
        print(num, end = ",")
        
        if num % 2 == 1:
            num = 3 * num + 1
        else:
            num = num / 2
    print(num)
    
colitz(123)