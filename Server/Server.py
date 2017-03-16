# -*- coding: utf-8 -*-
import socketserver
import json
from time import gmtime, strftime

"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

class ClientHandler(socketserver.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
		
		#Student code:
		username = '';
		
        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
			
			deliveryPayload = {'timestamp': '', 'sender': '', 'response': '', 'content': '',}
			deliveryPayload['timestamp'] = strftime("%Y-%m-%d %H:%M:%S", localtime())
            
            # TODO: Add handling of received payload from client
			
			payload = json.load(received_string) # decode the JSON object
			if payload['request'] == 'login' && username == '':
				username == payload['content']
				deliveryPayload['sender'] = 'server'
				deliveryPayload['response'] = 'info'
				deliveryPayload['content'] = 'Successful login - username: ' + username 
			else if payload['request'] == 'help':
				deliveryPayload['sender'] = 'server'
				deliveryPayload['response'] = 'info'
				deliveryPayload = 'Supported requests:\n' + \
									'login <username>\t\t\t-log in log in with the given username' + \
									'logout\t\t\t-log out' + \
									'msg <message>\t\t\t-send message' + \
									'names\t\t\t-list users in chat' + \
									'help\t\t\t-view help text'
			
			else if(username == ''): #Sjekk om alt stemmer... dessverre
				deliveryPayload['sender'] = 'server' # TODO: READ AND REMOVE, sender er ikke server når response er en 'message' - i.e brukeren sender en msg
				deliveryPayload['response'] = 'error'
				deliveryPayload = 'You must login first.'
				


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations are necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations are necessary
    """
    HOST, PORT = 'localhost', 9998
    print ('Server running...')

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
