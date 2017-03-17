
import json

class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
	    # More key:values pairs are needed
			'message': self.parse_message,
			'history': self.parse_history,
		# That is all of them!
        }

    def parse(self, payload):
        payload = json.loads(payload) # decode the JSON object

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            print('Response not valid, server not supporting')
            # Response not valid

    def parse_error(self, payload):
        print ("ERROR ", payload['content'])
    
    def parse_info(self, payload):
        print ("Info ", payload['timestamp'], "\n ", "Server: " , payload['content'])
    
    def parse_message(self, payload):
        print (payload['timestamp'], payload['sender'], ":")
        print ('   ', payload['content'])
	
    def parse_history(self, payload):
        print('-- CHAT HISTORY --')
        for message in (payload['content']):
            self.parse(message)
