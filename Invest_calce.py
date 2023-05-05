
def main():
    pass


def Tbill_gain(ytm=int,pv=int,fv=int,t=int,q=10):

    a= ((ytm/365)*t)
    b= ((ytm/365)*t)*q
    c= fv-pv

    print('interest on $100:',a)
    print('interest on $1000:',b)
    print('total return per $100: ',a+c)
    print('total return per $1000: ',b+c)
    

if __name__ == '__name__':
    main()