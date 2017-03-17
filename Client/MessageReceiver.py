# -*- coding: utf-8 -*-
from threading import Thread
from MessageParser import MessageParser

class MessageReceiver(Thread):
    """
    This is the message receiver class. The class inherits Thread, something that
    is necessary to make the MessageReceiver start a new thread, and it allows
    the chat client to both send and receive messages at the same time
    """

    def __init__(self, client, connection):
        """
        This method is executed when creating a new MessageReceiver object
        """

        # Flag to run thread as a deamon
        super(MessageReceiver, self).__init__()
        self.client=client
        self.connection=connection
        self.daemon = True
    def run(self):
        MsgParser = MessageParser()
        while True:
            data = (self.connection.recv(8192)).decode()
            if data:
               MsgParser.parse(data)
        pass
