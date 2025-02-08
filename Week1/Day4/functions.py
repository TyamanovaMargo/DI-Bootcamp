

# # Passing information (arguments,parametres) info a func

# # def say_hello(username):
# #     print(f"Hello {username}")

# # say_hello("Harry")


# def say_hello(username : str, language : str = 'EN') -> None: # default value
#     if language == "HE":
#         print(f"שלום {username}")
#     elif language == "EN":
#         print(f"Hello, {username}")
#     else: 
#         print(f"Ola, {username}")

# say_hello('Harry','RU')
# say_hello(language='PT', username = 'Luna')

# def calc (price, quan) -> int:
#     return price * quan        #without print it does show nothing

# def fav_colors():
#     fav_colors = ['blue','red', 'yellow']
#     for color in fav_colors:
#         print(f'I love {color}')
#     return f'Those are my fav colors'

# print(fav_colors())

# def get_country_info( country: str) :
#     if country == "Israel" :
#         oficial_name = 'State of Israel'
#         capital = 'Jerusalem'
#         population = 10000000
#     elif country == "Brazil":
#         oficial_name = 'Federative Republic of Brazil'
#         capital = 'Brazilia'
#         population = 21640000
#     else: 
#         print("invalid country")

#     return oficial_name, capital, population



# print(get_country_info( "Brazil"))     
# oficial_name, capital, population = get_country_info( "Brazil")

# Global and local  Scope

count_calculation = 100 # global scope

def calculation(a,b,count_calculation):
    addition = a + b
    substraction = a - b 
    count_calculation += 1
    return addition,substraction

print(calculation(8,5,count_calculation))
print(count_calculation)

clients = ['George','Jonh','Lisa']

def welcome (clients: list):
    for client in clients:
        print(f'Welcome {client}')
        clients['George'] = 'Dave'

def welcome_client():
    for i,client in enumerate(clients):
        clients[i] = f"Hello, {client}"


welcome (clients)
print(clients)

#*args not define quantity of arguments

def calculating(*args):
    return sum(args)

print(calculation(1,5,3,7))


#**kwargs
# k-key, w-words -args -arguments

def get_user_info(**kwargs):
    print(kwargs)

get_used_info(name = "Jonh",last_name = "Doe", age = 45, occupation = "Engeener")

matrix = []

for i in Matrix_string :
    