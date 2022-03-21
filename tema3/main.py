



def checkAPlusB():
    readA=open("./files/a.txt","r")
    readB = open("./files/b.txt", "r")
    readAPlusB = open("./files/a_plus_b.txt", "r")
    nA=readA.readline()
    readA.readline()
    nB= readB.readline()
    readB.readline()
    nAPlusB = readAPlusB.readline()
    readAPlusB.readline()
    ai=-1
    bi=-1
    abi=-1
    aj=-1
    bj=-1
    abj=-1
    aij=-1
    bij=-1
    abij=-1
    lineA=[]
    lineB=[]
    lineAPlusB=[]
    for i in range(0,2030):
        aModified=False;
        bModified=False;

        if(ai==bi):
            if(aj==bj):
                lineA = readA.readline().split(',')
                lineB = readB.readline().split(',')
                aModified=True
                bModified=True
            if (aj < bj):
                lineA = readA.readline().split(',')
                aModified=True
            if (aj > bj):
                lineB = readB.readline().split(',')
                bModified=True
        if(ai<bi):
            lineA = readA.readline().split(',')
            aModified=True
        if(ai>bi):
            lineB = readB.readline().split(',')
            bModified=True
        lineAPlusB = readAPlusB.readline().split(',')

        if(aModified):
            lineA1=[ float(lineA[0]), int(lineA[1]), int(lineA[2])]
            aij = lineA1[0]
            ai =   lineA1[1]
            aj =   lineA1[2]

        if(bModified):
            lineB1=[ float(lineB[0]), int(lineB[1]), int(lineB[2])]
            bij = lineB1[0]
            bi =   lineB1[1]
            bj =   lineB1[2]

        lineAPlusB1 = [float(lineAPlusB[0]), int(lineAPlusB[1]), int(lineAPlusB[2])]

        abij = lineAPlusB1[0]
        abi=lineAPlusB1[1]
        abj=lineAPlusB1[2]

        #print(lineA1+lineB1+lineAPlusB1)
        validation=-1
        if (ai == bi):
            if (aj == bj):
                if(aij+bij==abij):
                   validation=1
                else:
                    validation=0
            if (aj < bj):
                if (aij == abij):
                    validation=1
                else:
                    validation=0
            if (aj > bj):
                if (bij == abij):
                    validation=1
                else:
                    validation=0
        if (ai < bi):
            if (aij == abij):
                validation=1
            else:
                validation=0
        if (ai > bi):
            if (bij == abij):
                validation=1
            else:
                validation=0
        if(validation==-1):
            print("2000")
        if(validation==0):
            print("nu sunt egale")
            print(lineA1,lineB1,lineAPlusB1)

    #     if(ai==bi and ai ==abi)
    #         if (int(lineA[1]) == int(lineB[1]) and int(lineA[1]) == int(lineAPlusB[1]) and
    #             int(lineA[2]) == int(lineB[2]) and int(lineA[2]) == int(lineAPlusB[2]) and
    #             float(lineA[0])+float(lineB[0]) == float(lineAPlusB[0])
    #             ):
    #             print(lineA[1] + " ok\n")
    #         else:
    #             print(lineA[1] + " err\n")
    #
    #
    #     lineA = readA.readline().split(',')
    #     lineB = readB.readline().split(',')
    #     lineAPlusB = readAPlusB.readline().split(',')
    #     print(lineA+lineB+lineAPlusB)
    #     if(int(lineA[1])==int(lineB[1]) and int(lineA[1])==int(lineAPlusB[1]) and
    #         int(lineA[2]) == int(lineB[2]) and int(lineA[2]) == int(lineAPlusB[2]) and
    #             float(lineA[0])+float(lineB[0]) == float(lineAPlusB[0])
    #     ):
    #         print(lineA[1]+" ok\n")
    #     else:
    #         print(lineA[1]+" err\n")
    #
    #
    #
    #
    # lineA=readA.readline();
    # splitline=lineA.split(',')
    #
    #
    # print(int(splitline[2]))





def main():
    checkAPlusB()


if __name__ == '__main__':
    main()


