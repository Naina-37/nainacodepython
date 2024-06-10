#   1 A car is moving at a speed of 90 km/h. Calculate the distance it travels in 12 seconds.
speed = 90
time =12
speed = speed * 5/18
length = speed * time 
print("distance travelled by car :   " ,length)


# 2 A truck is traveling at a speed of 75 km/h. Calculate the distance it covers in 25 minutes. Then, calculate how much further it would travel if it increased its speed by 20% for the same amount of time.
speed = 75
time = 25
speed = speed * 5/18
time = time*60
#DISTANCE COVERED BY TRUCK 
distance = speed * time 
#CONVERT IN Km
distance=distance/1000  
print("distance covered by truck:  " , distance )
#SPEED INCREASE BY 20%
increase_speed = speed * 1.20   # 20% increase

#updated_speed = increase_speed * (5/18)
updated_distance = increase_speed * time #updated_speed # doubt 
updated_distance = updated_distance/1000
print("DISTANCE AFTER SPEED INCREASE<<<<<<<<<<<<<  :  ",updated_distance)
#increased_speed = speed * 1.20  # 20% increase



# 3 A train travels at a speed of 100 km/h for 2 hours and then reduces its speed by 30 km/h for the next 1.5 hours. Calculate the total distance traveled by the train.
speed = 100
time = 2
distance=speed*time
print("Intial distance is : ", distance)
decrease_speed=30
update_speed=speed-decrease_speed
time=1.5
updated_distance=update_speed*time
print("UPDATE of distance : ",updated_distance)
total_distance=distance+updated_distance
print("total distance will be :",total_distance)