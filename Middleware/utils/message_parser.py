# Get parameters from message
def get_params(message):
	action = message.split()[0]
	params = (message.split()[1]).split('&')

	return (action, params)