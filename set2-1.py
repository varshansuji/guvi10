def power(suj,mai):
    if(mai==1):
        return(suj)
    if(mai!=1):
        return(suj*power(suj,mai-1))
suj=int(input("Enter suju value: "))
mai=int(input("Enter mai value: "))
print("Result:",power(suj,mai))
