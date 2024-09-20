calls = 0

def count_calls():
    global calls
    calls +=1

def string_info(string):
    count_calls()
    return len(string), string.lower(), string.upper()

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [i.lower() for i in list_to_search]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)