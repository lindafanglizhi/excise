data ={
'username': '${ENV(UserName)}',
            'password': '${get_encrypt_password()}'}

env=data['password']
print(type(env))

pas=env[2:-1]


def get_encrypt_password():
    print('hello')


eval(pas)

