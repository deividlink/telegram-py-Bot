import telepot
import requests
token_owm="token OWM"
dict_word={
        "bloken clouds":"clima fechado",
        "light rain":"chuva leve"
        }
bot=telepot.Bot("Seu token do botFather")

def req(msg):
    user=msg['chat']
    print("Id:",user['id'])
    print("Nome:",user['first_name'],user['last_name'])
    print("Mensagem:",msg['text'])
    mens=msg['text'].lower()
    if mens=="iniciar":
        bot.sendMessage(user['id'],"""Ola,Bem vindo
        Precisa de ajuda Digite Ajuda""") 

        print("Mensagem: {} enviada para id: {}".format("Ola,Bem vindo",user['id']))
    if mens=='clima':
        url="http://api.openweathermap.org/data/2.5/weather?appid={}&q=cidade,pais".format(token_owm)
        clima=requests.get(url).json()
        status=clima['weather']
        for x in status:
            z=x['description']
            clima_m=dict_word[z]
            if clima_m=="chuva leve":
                bot.sendMessage(user['id'],"https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSIl5RUb9etgTng_79506rAxD8QGZox6lODMgSArmHmRVt66oM2")
            bot.sendMessage(user['id'],"Clima:{}".format(clima_m))
    if mens=="linguagem":
        bot.sendMessage(user["id"],"https://www.python.org")
    if mens=="ajuda":
        bot.sendMessage(user["id"],"""Comandos:
                Iniciar - Memsagem de Bem vindo
                Clima - mostra o clima
                linguagem- mostra a linguagem""")
bot.message_loop(req)
while True:
        pass
