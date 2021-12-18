import socket
multibroadcast="239.255.255.250"
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("","10240"))
s.setsockopt(socket.IPPROTO_UDP,socket.IP_MULTICAST_TTL,255)
s.setsockopt(
  socket.IPPROTO_IP,
  socket.IP_ADD_MEMBERSHIP,
  socket.inet_aton(multibroadcast) + socket.inet_aton("")
)
# import  socketserver
# socketserver.UDPServer

