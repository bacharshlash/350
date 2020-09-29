import socket 
from datetime import datetime
import struct 
#the following are from Rfc 868 
port= 37
receive_buffer_size= 32
#choosing servers
server_1= "time-b-g.nist.gov"
server_2= "time-a-b.nist.gov"
#create socket and connect it to corresponding server and port
mysocket_1 = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
mysocket_1.connect((server_1,port))
mysocket_2 = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
mysocket_2.connect((server_2,port))
#receive response
response_string_1 = mysocket_1.recv( receive_buffer_size )
response_string_2 = mysocket_2.recv( receive_buffer_size )
#closing socket
mysocket_1.close
mysocket_2.close
#getting IP address of each server 
ip_1= socket.gethostbyname(server_1)
ip_2= socket.gethostbyname(server_2)  
#getting int from bytes
time_1=int.from_bytes(response_string_1, byteorder='big')
time_2=int.from_bytes(response_string_2, byteorder='big')
#converting from int to an actual readable time clock while also subtracting 70 years. 
t_1= datetime.fromtimestamp(time_1 - 2208988800)
t_2= datetime.fromtimestamp(time_2 - 2208988800)
#now getting the time difference between the two 
diff= t_1 - t_2
#now printing everything (ip address of each server, time of each server, and time difference of the servers)
print("IP address of server 1 is : ", ip_1)
print("IP address of server 2 is : ", ip_2)

print ("The time of server 1 is: ", t_1)
print ("The time of server 2 is: ", t_2)

print("the time difference is: ", abs(diff))
