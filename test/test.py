
def one():
   for i in range(1 , 100):
       print(str(i))


def fa(b):
    if b == 1 :
        return 1
    else:
        return b*fa(b-1)








def zoj(n):
    if n%2 == 0 :
        print( "z")





    else:
        print("f")

if __name__ == '__main__':
 print(fa (5))






