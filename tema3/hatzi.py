def memorareEconomicPeLinie(path):
    readA = open(path, "r")
    nA = readA.readline()
    readA.readline()
    memorareEco=[]
    for i in range(int(nA)):
        memorareEco.append([])    #fac 2000 vectorii goli sa ii pot apela dupa
    for readLine in readA:        #citesc toate liniile din fisier
        if (readLine != '\n'):    #asa e ca imi dadea eroare la final de fisier
            line = readLine.split(',') #splitu
            lineij = float(line[0])   #iti dai si singur seama ce fac aici
            linei = int(line[1])
            linej = int(line[2])
            exists=False
            if(linej<=linei):
                for element in memorareEco[linei]:
                    if(element[1]==linej):
                        element[0]=element[0]+lineij
                        exists=True
                if(exists==False):
                    memorareEco[linei].append([lineij,linej]) # ii dau apend la [valoare,
    #print(memorareEco[3])
    #print(memorareEco[0:5])
    return memorareEco
def memorareEconomicPeColoana():
    readA = open("./files/a.txt", "r")
    nA = readA.readline()
    readA.readline()
    memorareEco = []
    for j in range(int(nA)):
        memorareEco.append([])  # fac 2000 vectorii goli sa ii pot apela dupa
    for readLine in readA:  # citesc toate liniile din fisier
        if (readLine != '\n'):  # asa e ca imi dadea eroare la final de fisier
            line = readLine.split(',')  # splitu
            lineij = float(line[0])  # iti dai si singur seama ce fac aici
            linei = int(line[1])
            linej = int(line[2])
            exists = False
            if(linej<=linei):
                for element in memorareEco[linej]:
                    if (element[1] == linei):
                        element[0] = element[0] + lineij
                        exists = True
                if (exists == False):
                    memorareEco[linej].append([lineij, linei])  # ii dau apend la [valoare,
    print(memorareEco[0])
    # print(memorareEco[0:5])
    return memorareEco




def memorareEconomicDacaSuntInOrdine():
    readA=open("./files/a.txt","r")
    nA=readA.readline()
    readA.readline()
    a=4
    b=5
    lasti=0
    lastj=0
    alli=[]
    memorareEco=[]
    lastwritei=0
    for readLine in readA:
        if(readLine!='\n'):
            line=readLine.split(',')
            lineij=float(line[0])
            linei=int(line[1])
            linej=int(line[2])
            if(lasti>linei):
                print("don't good")
                print(str(lasti)+" "+str(linei))
            if(lasti==linei):
                a=[lineij,linej]
                alli.append(a)
                lasti=linei
            else:

                while(lastwritei<lasti-1):
                    memorareEco.append(0)
                    lastwritei+=1
                memorareEco.append(alli)
                alli=[]
                alli.append([lineij, linej])
                lastwritei=lasti
                lasti=linei
    memorareEco.append(alli)

    print(memorareEco[0])
    print(memorareEco[1])
    print(memorareEco[2])
    print(memorareEco[3])
    print(memorareEco[4])
    print(memorareEco[5])
    print(memorareEco[6])
    print(memorareEco[7])
    print(memorareEco[2016])
    print(len(memorareEco))

def value(matrice,i,j):
    try:
        for element in matrice[i]:
            if(element[1]==j):
                return element[0]
        return 0
    except:
        return 0

def inmultireAB(matrice):
    inmultire = []
    for i in range(len(matrice)):
        inmultire.append([])

    for i in range(len(matrice)):
        print(i);
        for j in range(0,len(matrice)+1):
            print(i)
            print(j)
            inmultirepozitie=0
            for ipoz in range(int(len(matrice)/2)+1):
                inmultirepozitie+=value(matrice,i,ipoz)*value(matrice,ipoz,j)
            if(inmultirepozitie!=0):
                inmultire[i].append([inmultirepozitie,j])
       # print(inmultire)
    print(inmultire)

def inmultireABv2(matriceA,matriceB):
    inmultire = []
    for i in range(len(matriceA)):
        inmultire.append([])
    for i in range(0,len(matriceA)):
        print(i)
        for j in range(0,len(matriceA)):
            sum=0
            for k in range(0,i+2):
                sum+=value(matriceA,i,k)*value(matriceB,k,j)
            if sum!=0:
                inmultire[i].append([sum,j])
    print("////////////")
    print(inmultire)



if __name__ == '__main__':
    matriceA=memorareEconomicPeLinie("./files/test.txt")
    #matriceB=memorareEconomicPeLinie("./files/A.txt")
    inmultire=inmultireABv2(matriceA,matriceA)

    #print(matrice[])

    #inmultireAB(matrice)
    a=0
    b=0
    c=[0,4,2]
    c.append(0)
    print(c)
