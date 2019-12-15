
def strToInt(string):
    x=0
    flag = 0
    if(string[0]=='-'):
        flag=1
        
    for i in range (0,len(string)):
                    if string[i].isdigit():
                        x+=int(string[i])*10**int(len(string)-i-1)
                        print('In strToInt',i,x)
    if (flag ==1):
        return (-1)*x
    else:
        return x

print(strToInt('-14'))
