# -*- coding: utf-8 -*-
import socket
import json
import time
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.host=host
        self.server_port=server_port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receiver=MessageReceiver(self, self.connection)

        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        receiver=MessageReceiver(self, self.connection)
        receiver.start()
        print("Hello and welcome to a highly functional chat service")
        while (1):
            userInput = input()

            try:
                request, message = userInput.split(' ', 1)

            except (ValueError, KeyboardInterrupt, IndexError):
                message = None
                request = userInput
            
            payload = {'request': request.lower(), 'content': message}
            self.send_payload(json.dumps(payload))
            if (payload['request']=='logout'):
                time.sleep(0.5) 
                self.disconnect()


    def disconnect(self):
        self.connection.shutdown(1.5)
        self.connection= socket.close()
        print('Connection successfully terminated')
        exit(0)
        pass

    def receive_message(self, message):
        incoming=json.loads(message)

        pass

    def send_payload(self, data):
        # TODO: Handle sending of a payload
        try:
            self.connection.send(data.encode())

        except Exception as shitHappend:
            print (shitHappend)
            print ("Message not sent")

        pass
        
    # More methods may be needed!


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
    


