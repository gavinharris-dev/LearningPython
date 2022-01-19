
def addOne(num):
    return num + 1


def subOne(num):
    return num - 1

def getNumber(attempts):  
    try:
        return int(input("Pick a number: "))
    except:
        if (attempts > 2):
            raise Exception("Learn your numbers")
        
        print("Enter a number please!")
        attempts += 1
        return getNumber(attempts)

num = getNumber(0)


print( subOne(num) )

