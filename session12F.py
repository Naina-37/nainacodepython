from session11C import Vehicle
from session11D import Driver
from session12 import Customer
from session12E import Ride

# Driver Application
driver = Driver()
driver.add_driver_details()

# Customer Application
customer = Customer()
customer.add_customer_details()

# Server
ride = Ride()
ride.add_ride_details()
ride.link_customer(customer)
ride.link_driver(driver)

print("RIDE BOOKED....")
ride.show()