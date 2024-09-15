def fileReader(fileName0):
    f0 = open(fileName0, "r")
    res = []
    for i in range(600):
        x = f0.readline()
        res.append(removeUnwantedSpace(str(x)))
    return res

def removeUnwantedSpace(string):
    res = ""
    N = len(string)
    if N == 0:
        return ""
    for i in range(N-1):
        if string[i] != " " and string[i+1] != " ":
            res += string[i]
        
        if string[i] != " " and string[i+1] == " ":
            res += string[i]
            res += " "
    res += string[N-1]
    return res
    
def mergeTheList(twoDList):
    res = ""
    for i in twoDList:
        if i != '\n':
            res += str(i)
    return res
    
def countOccurences(key,inSentence):
    return inSentence.count(key)
    
def findMatches(sentence,keywords):
    res = []
    for i in keywords:
        row = [i]
        cnt = countOccurences(i,sentence)
        row.append(cnt)
        res.append(row)
        
    return res

def checkRedundant(L,word):
    match = 0
    for i in L:
        if word == i:
            match = 1
            break
    return match
    
        
def findKeywords(sentence):
    i = 0
    res = []
    N = len(sentence)
    while(i <= N - 1):
        while(i <= N - 1 and sentence[i] == ' '):
            i += 1
        if i <= N - 1 and sentence[i] != " ":
            word = ""
            while(i <= N - 1 and sentence[i] != " "):
                word += sentence[i]
                i += 1
            if checkRedundant(res,word) == False:
                res.append(word)
    return res
    
    
def sortTheList(x):
    #[[a,113],[b,23],[f,123]] ==> [[b,23],[a,113],[f,123]]
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j][1] < x[j+1][1]:
                tmp = x[j]
                x[j]= x[j+1]
                x[j+1]=tmp
    return x

def normalAvg(x):
    N = len(x)
    s = 0
    for i in range(N):
        s = s + x[i]
    return s/N

def matchPercentage(match0,match1):
    res = []
    for i in range(len(match0)):
        for j in range(i,len(match1)):
            if match0[i][0] == match1[j][0]:
                row = []
                row.append(match0[i][0])
                row.append(match0[i][1])
                row.append(match1[j][1])
                row.append(abs(match0[i][1] - match1[j][1]))
                res.append(row)
    return (1 - normalAvg(extractColumn(res,3))/normalAvg(extractColumn(res,1)))*100,(1 - normalAvg(extractColumn(res,3))/normalAvg(extractColumn(res,2)))*100
    
def extractColumn(T,index):
    R = len(T)
    col = []
    for i in range(R):
        col.append(T[i][index])
    return col
    
import os 
import sys
import subprocess
# Access command-line arguments
args = sys.argv

path = subprocess.check_output(['pwd']).decode().strip()

#path = "/home/abhilash/Documents/DaaLabChecker/daalab-02/longestSegment/"
dir_list = os.listdir(path)
print("Current Path assigned: ", path)
print("Total files = ",len(dir_list)-2)
#input threshold
threshold = int(args[1])

copiesLeaks = []

def unique(list1):
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    for x in unique_list:
        print(x)
        
for i in range(len(dir_list)):
	for j in range(i+1,len(dir_list)):
		if dir_list[i]!='checkPlagForAll.py' and dir_list[j]!='checkPlagForAll.py':
			p = (fileReader(dir_list[i]))
			q = (mergeTheList(p))
			keys = ['end','push_back','find','std','unordered_set','public','class','static','void','nextInt','long','hasNextInt','+=','-=','++','--','*=','/=','+','-','*','/','^','printf','print','int','float','vector',':','def','break','==','|','||','&&','if','<=','=','<','>','>=','for','while','do','else','cout','cin','[','{','.',',','#',"!",'%','&','*','(','append','insert','enumerate','push','pop','return','main']

			T0 = ((findMatches(q,keys)))
			p = (fileReader(dir_list[j]))
			q = (mergeTheList(p))
			T1 = ((findMatches(q,keys)))
			Res = matchPercentage(T0,T1)
			if (Res[0]+Res[1])/2 > threshold:
				print(dir_list[i],"<=>",dir_list[j],">>",Res)
				copiesLeaks.append(dir_list[i])
				copiesLeaks.append(dir_list[j])
print("............................................")
print("Plagiarism List --")
print(unique(copiesLeaks))
print("............................................")
