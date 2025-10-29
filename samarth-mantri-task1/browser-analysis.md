1.(a):-

Screenshots.



1.(b) :-

Request header basically is the piece of information sent by the client (browser) to the server which basically contains information about the device, browser type ,supported content types, compression algorithms, etc. When we compare the http and https there are some common  or we can say standard request header like Accept-Encoding, User-Agent. But when we come towards the differences ,in HTTPS, there are some additional headers starting with ‘Sec-’, which indicate that they are sent only in secured manner for additional privacy and security. These are automatically sent  by the browser to the server. Some of the examples are Sec-Ch-Ua which basically is the request header, it gives limited information about the browser with privacy and the friendly and proper structured way to the server. Similarly there are many more security based request header in the https which are not there in the http.



1.(c):-

In the HTTP we can see the data in the form of the plain text i.e. normally which means that if there is any middle system or network of systems then the data can be seen by any client in that network or that middle agent. But in HTTPS the data cannot be seen by the other clients of that network as the data get encrypted and can only be seen by the users to whom the server or the client wants to send or show.



1.(d):-

The HTTPS is more secure than the HTTP because in HTTPS the data to be sent or received by the client or server is encrypted and cannot be read by the other users in that network. While, in the HTTP the data is sent or received in the same way without any encryption, so can be accessed by the other user in that network too. Hence HTTPS is more secure than the HTTP.



2.(a):-
There were 8 requests made on the http://neverssl.com, 162 on the https://github.com , 101 on the https://youtube.com
The above data is the current information according to my PC but , the number went on increasing for the https and not for the http.



2.(b):-
i - http://neverssl.com :- JS, Document, etc.

ii - https://youtube.com :- CSS, XHR, Document, HTML, JS, font , media , etc (some of these not in the screenshot because there are more numbers of requests that cannot be included in it.)
iii - https://gitHub.com :- Document, CSS , JS, Font, PNG , JPEG, etc (some of these not in the screenshot because there are more numbers of requests that cannot be included in it.)



2.(c):-

Among the 3 of them the website https://github.com made more number of requests when compared to the other 2 because when we load github.com it requires more number of resources to build the page of its website.



3(a):-

Load time (according to the screenshots)

i :- http://neverssl.com :- 445 ms.

ii - https://youtube.com :- 5.22 s.

iii - https://gitHub.com :- 2.28 s.

Load time when reloaded the website

i :- http://neverssl.com :- 450 ms.

ii - https://youtube.com :- 4.52 s.

iii - https://gitHub.com :- 1.28 s.





3(b):-

(According to the reloaded data)

in all the three of the websites the highest time was taken by the main Document file to get loaded. But as the number of requests went on increasing it took a lot time than others but that are not included in the load time.



3(c):-
i :- DNS lookup : it is the time taken by the browser to find the IP Address of that website for that particular request. In Some requests the timing is non zero which means the browser required time to find the IP address but in some websites its in micro seconds or 0 it means that the particular IP address is already fetched and is present in the browser cache memory (sometimes in the OS cache or Local DNS resolver) or the request was in the same domain/server as that of previous request. For the requests that it have chosen it has taken no time in neverssl.com while has taken 210.40 ms and 129.47 ms respectively on the youtube.com and github.com.



ii :- Connection Time is the time the browser takes to establish a connection with the server for a particular request. It usually consists of the initial time (TCP connection) to connect with server and the time taken for encryption and verification of the server in the HTTPS , while we do not have the encryption time in the HTTP



iii :- TTFB (Time to First Byte) is the time the browser waits after sending a request until it receives the first byte of the response from the server. But I was unable to see the TTFB section which means the browser didn’t need to wait for the server response.This can happen if the resource was cached, the connection was reused, the response was extremely fast, or the request spent most of its time stalled/queued.





