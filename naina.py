# MULTI value Container
#MVC  :LIST
#which can be created,once created
# MUTABLE

friends=["john","jennie","jim","jack","joe",1001]
print(friends,type(friends),id(friends))
print(friends[0],type(friends[0]),id(friends[0]))
print(friends[1],type(friends[1]),id(friends[1]))
print(friends[2],type(friends[2]),id(friends[2]))
print(friends[3],type(friends[3]),id(friends[3]))
print(friends[4],type(friends[4]),id(friends[4]))
# let us change....
#you will get an error 
friends[0]="jhon"
print(friends,type(friends),id(friends))
print(friends[0],type(friends[0]),id(friends[0]))