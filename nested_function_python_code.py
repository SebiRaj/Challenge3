def function11(a,b,c,d):
    c=d
    b=c
    a=b
    key_1=a/b/c
    print(key_1)
    def function12(x,y,z):
        z=a
        y=z
        x=y
        key_2=x/y/z
        print(key_2)
        print(a)
    return function12(3,4,5)
function11(1,4,5,5000)