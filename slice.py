city= "Nairobi"
print(city[:5])
print(city[2:])
print(city[-1:])

f_name = "Martin Mbugua" #small letters
# .upper() convert to upper case
print(f_name.upper())

s_name= "MARTIN MBUGUA CHEGE"
# .lower() convert to lower case
print(s_name.lower())

#concatination-converting from one data type to another
#int->float   float(x)
#float-> int  int(x)
#int-> str   str(x)

number=5
print(str(number))

x=4 #x is an integer
print(float(x))

y=3.12334467676767676
print(int(y))

f_name = "Eren"

s_name = " Yeagar"

full_name = f_name + s_name

print(full_name)

name="Martin Mbugua"
print(name.replace('M','Z'))


msg="Give your hearts for humanity"
print(msg.split())

print(len(msg))
