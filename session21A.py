quote ="search the canadle rather than cursing for darkness"
print(quote[1])
print(quote[-1])
print(quote[-8:])
email=input("enter email")
if '@' in email and "." in email:
    print("Email is well formed")
else:
    print("email is not well formed")
contacts=["john","sia","kia","joe","jackson"]
search=input("enter search keyword")
for contact in contacts:
    if search in contact:
        print(contact)