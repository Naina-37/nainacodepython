import hashlib

password=input("enter your password")
print("password is:",password)
password=password.encode('utf-8')
password_encrypted=hashlib.sha256(password).hexdiges
