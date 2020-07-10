#SORU 1
#ay={1:"Ocak",2:"Subat",3:"Mart",4:"Nisan",5:"Mayıs",6:"Haziran",7:"Temmuz",8:"Agustos",9:"Eylul",10:"Ekim",11:"Kasım",12:"Aralık"}
#u=int(input("Bir gün girin:"))
#m=int(input("Bir ay girin :"))
#t=int(input("Bir yıl girin :"))
#print(u,ay[m],t,sep="-")


#SORU 2
#def fak(sayi):
#    faktor=1
#    for i in range(1, sayi+1):
#        return faktor
# def f(x):
#    toplam=0
#    if(x>=9 and x<16):
#        for i in range (2, (2*x)+1, 2):
#            toplam = toplam+i:
#        elif(x>=0 and x<9):
#            for i in range(2, (3*fak(x))+1, 2):
#                toplam = toplam+i:
#            return toplam
# sayi= int(input("bir sayı girin: "))
#    if (sayi<0 and sayi>16):
#        print("geçerli bir sayı girin: ")
#    else:
#        print("sonuç => ", f(sayi))


#SORU 3
#def sifre(A,B):
#  result = []
#  x = 0
#  for i in range(0,3):
#    x = 0
#    for j in range(0,3):
#      x += A[i][j]*B[i][j]
#    result.append(x)
#  print(result)
# dictionary = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
# matrisA = [
#  [1,2,-1],
# [2,5,2],
# [-1,-2,2]]
# name = "umutcavlamaz"
# matrisB = []
# for i in range(0,3):
#  matrisB.append([dictionary[str(name[i])],dictionary[str(name[i+1])],dictionary[str(name[i+2])]])
#sifre(matrisA,matrisB)


#SORU 4 
#u=[] #Boş bir liste tanımladım.
#for m in range(1,16): 
#   if m > 1:  
#       for t in range(2,m):  
#           if (m % t) == 0:  
#               break  
#       else:
#           u.append(m)
#print(u)