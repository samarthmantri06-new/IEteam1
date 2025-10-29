Exaplination of the code:

(A) The DHCP server:-
	i - __init__() :- creats an list of IP address and also an empty list which could later maintain a track of the IP address that has already been assigned to a MAC address.
	ii - handle_dhcp_disocer :- when a client says I need a Ip address this function offers the topmost available IP address to the Client.
	iii - handle_dhcp_request :- This function once received the confirmation from the client gives the IP address and then removes that particular IP address from the list of available once and add it to the other list.

(B) The DNS Server :-
	i - __init__() :- in this it maintains a record of the name of the host and the IP address assigned to it by the DHCP server. It is useful when one wanted to get connected to the other.
	ii - add_record "- adds a new name in the dictionary data type used in above function.
	iii - resolve() :- it looks for the IP address for a given host name to be connected. It is also the main function of the DNS server.

(c) Clients ;-
	i - __init__() :- it creates a new client with a name, which will later get linked with the DHCP and the DNS server will get assigned with a MAC address, then will get assigned with the IP address whenever wanted to make a communication.
	ii - generate_mac() :- Assigns new client a random but unique MAC address.
	iii - boot() :- stimulates teh client turning on and requesting an Ip address, it sends DHCP discover, gets an offer , sends DHCP request to assign me the offered IP address and then the IP address get assigned.
	iv - resolve_hostname() :- asks the DNS to find the IP address for the Given Host name, so that the devices can communicate.
	v - ping() - simulates sending a "ping" to another IP address waiting for the reply, this is important because it ensures that the 2 devices are on the same network and can communicate with each other.

the remaining is the Work flow.