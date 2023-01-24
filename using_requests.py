import requests # import the library - we may need to pip install requests

# we need a function that can make a request to an API to get some data
def getData(user_id):
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    # we use the requests library to get data
    response = requests.get(url) # this will get the JSON from the API
    print(type(response))
    # we need to get the JSON from the response
    r_dict = response.json() # convert it to a Python dictionary
    return r_dict # its a good idea to let functions return their values

if __name__ == '__main__':
    # ask the user for a number
    n = input('Which user (1-10)? ')
    n_num= int(float(n)) # make sure it is an integer
    if n_num>0 and n_num<11: # make sure it is beween 1 and 10
        # pass that number into the function
        result = getData(n_num) # we need to invoke our function
        # we can strip off the bits of data we are interested in
        user_name  = result['name']
        user_email = result['email']
        user_street = result['address']['street'] # access the nested dictionary
        print(f'User {user_name} has email {user_email} and lives at {user_street}')