(1) :-

Top 5 protocols -- percentage 

Ethernet -- 100%
Internet Version Protocol 6 -- 79.5%
User Datagram protocol -- 49.6%
QUIC IETF -- 47.3%
Transmission Control Protocol -- 29.8%

Work of the Protocols;
Ethernet - getting the data to the right device within the local network using MAC addresses.
Internet Version Protocol Version 6- it's job is to assign different devices unique IPv6 address and route data packets across the internet to reach the destination.
User Datagram protocol - it sends data quickly without checking for errors or guaranteeing the delivery of the packets.
OUIC IETF - used to combine speed and reliability.
Transmission Control Protocol - it ensures reliable and ordered delivery of the data.

(2) :-
i- 
Domain being quired :- www.google.com
DNS server IP address :-172.25.136.245
Response IP Address :- 172.25.136.212
Response time :- 333.771 ms.

ii-
Domain being quired :- android.clients.google.com
DNS server IP address :-2409:40f2:315d:77fb:9146:b49e:ad15:d47f
Response IP Address :-2409:40f2:315d:77fb::f6
Response time :- 2.518328 s.

iii-
Domain being quired :- google.com
DNS server IP address :-172.25.136.245
Response IP Address :- 172.25.136.212
Response time :- 167.215 ms.

(3) :-
whenever 2 computers wants to communicate with each other then first they have to make a reliable connection with each other, this is done using a TCP three way handshake by sending each other 3 special types of the flags namely SYN , SYN ACK , ACK.
i - [SYN] - this is a flag sent by the client to the server to initiate the connection and synchronise the sequence numbers.
ii - [SYN, ACK] - it the flag sent by the server back to the client, so that the client understands that the server has received clients message and sent acknowledgement and also its starting sequence number so as to synchronise.
iii - [ACK] - it is sent by the client to the server, in this the client acknowledges the server that about the received message and the confirmation of the connection establishment.

After this the 2 computers can send data to each other.

hence we need this handshake to establish a successful connection between 2 computers.

(4)
Yes , we can read the actual request or response in the HTTP 
NO, i also cannot see read the encrypted data because it is not understandable when we filter out with tls.
we cannot read the data because the packet was captured when the data transmission was taking place where the data gets encrypted by the https. 
