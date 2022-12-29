import csv
from csv import reader
import  hashlib 

hash_password_to_password={}
with open('password2.csv', 'w', newline='') as csvfile:
    
    fieldnames = ['first_name', 'hash']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for password in range(1,1000):
        hashing_number=hashlib.sha256(b'%i'%password)
        hashhex=hashing_number.hexdigest()
        #create dic
        hash_password_to_password[hashhex]=password
        #write csvfile
        writer.writerow({'hash':hashhex,'first_name':password})
with open('password.csv') as  f:
    password_singer=reader(f)
    for row in password_singer:
        name_users=row[0]
        
        for key_or_hash in row[1:]:
            print(key_or_hash)
            if  key_or_hash in hash_password_to_password.keys():
                print(name_users,':',hash_password_to_password[key_or_hash])
            else:
                print("not exsit in dic:".format(key_or_hash))
        
