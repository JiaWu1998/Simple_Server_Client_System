# Simple_Server_Client_System

This project is a client-server mode file downloading system. A server will hosts a list of files which clients can download. In addition to the downloading capabilities, the client can also view the list of files that the server has to offer. This system is also good for multiple requests from multiple clients. 


To run a sample server/client do the following:
1. type 'make setup' 
2. open 2 seperate terminals(use one for server and one for client)
3. choose one terminal and type 'python3 server/server.py'
4. choose the other terminal and type 'python3 client_0/client.py'
5. choose a username for the client terminal and continue with the help of the manual from the client terminal
6. when you are done, type 'make clean'
*NOTE: All log files are in server and client folders. If you do a "make clean", it would be wiped out along with the server and client folders

To run evaluation 1 do the following:
1. type 'make eval_1'

To run evaluation 2 do the following:
1. type 'make eval_2'

To run evaluation 3 do the following:
1. type 'make eval_3'

To run evaluation  do the following:
1. type 'make eval_4'