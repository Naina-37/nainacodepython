password=input("Enter your password:")
print(len(password))
p1=password.strip()
print(p1,len(p1))
data="000003829"
print(data.strip("0"))
print(data)

amount=35.540000
new_amount=float(str(amount).strip("0"))
print(new_amount,type(new_amount))
quote="search the candale rather than cursing darkness"
s1=quote.replace("t","k")
print(quote)
print(s1)
message="No internet connection"
print(message)
print(message.center(50))
print(message.ljust(50))
print(message.rjust(50))
amount=545
data=str(amount).zfill(8)
print("data is:",data)
quote="search the candle rather than cursing the darkness"
idx1=quote.find("the")
idx2=quote.find("dark")
print("idx1:",idx1)
print(quote[idx1:idx1+3])
print(quote[idx2:])
idx3=quote.rfind("the")
print(idx3)
print(quote.index("the"))
print(quote.rindex("the"))
