# -*- coding: utf-8 -*-
space=" ";
print("Buenos dias")
name=input("Como te llamas?:")
last=input("Tu apellido:")
location=input("Donde estas?:")
age=input("Tu edad:")
agestr=int(age)
if agestr>=18:
    print("Ahora se que eres"+space+name+space+last+", tienes "+age+" años. eres mayor de edad, y que estas en "+location+"."+"\n"+"Hasta pronto")
else:
    print("Ahora se que eres"+space+name+space+last+", tienes "+age+" años. eres menor de edad, y que estas en "+location+"."+"\n"+"Hasta pronto")

