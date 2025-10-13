
# Function to validate states of tasks
def state_check(request):
    valid_states = ['to do', 'in progress', 'completed']
    if request.json['state'] not in valid_states:
        raise ValueError('state must be either: to do, in progress, completed')
