#!/user/bin/env python
import sys, socket 
result = socket.getaddrinfo(sys.argv[1], None)
print(result)
print(result[0][4])