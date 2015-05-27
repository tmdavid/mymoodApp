__author__ = 'dtorrejon'

lista = [1,2,2,3,3,4,5,5,6,7,8,9,9,9,9]

def getunique(unique):
    i = 1
    while(i<len(unique)-1):
        while(unique[i-1]==unique[i] and i<len(unique)-1):
            unique.remove(i)
            print unique
        if(unique[i-1] != unique[i]): i+=1
    return unique

print "ordered"
getunique(lista)

listb = [2,3,4,5,1,6,2,3,4,7,4,8,9,1]

def getuniqueordered(unique):
    unique.sort()
    getunique(unique)
    return unique


print "unordered"
getuniqueordered(listb)
