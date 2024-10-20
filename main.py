stroka=input("Введите строку:") 

i=0 
for char in stroka.lower(): 
     if char !="а" and char!="о"and  char!="у"and  char!="ы"and  char!="э"and  char!="я"and   char!="е"and   char!="ё"and   char!="ю" and   char!="и": 
      char=i 
      print("Индекс согласной буквы :", i)
     i+=1


   
   
