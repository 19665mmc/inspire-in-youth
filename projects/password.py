import random
print("Welcome to Password Generator")
num_password=int(input('Number of passwords'))
length_password=int(input('Number of characters in password'))
characters='65657575hvfhuifdhviufvfdvif'
print('\n Here are your passwords')
for password in range(num_password):
    password=''
    for c in range(length_password):
        password+=random.choice(characters)
    print(password)




