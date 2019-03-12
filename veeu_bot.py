import requests,time,random,json

head = {
    "Host": "www.veeuapp.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.10.0"
}

header = {
    "Content-Type":"application/json; charset=utf-8",
    "Content-Length": "140",
    "Host": "www.veeuapp.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.10.0"
}
headDATA2 = {
    "Host": "www.veeuapp.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.10.0"
}

headlog = {   
    "Content-Encoding": "gzip",
    "Content-Type":"application/json; charset=utf-8",
    #"Content-Length": 940,
    "Host": "www.veeuapp.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.10.0"
    }

video = {
    'locale': 'in_TH',
    'task_extra_info': '',
    'task_name': 'vip_watch_video_ball_01',
    'timezone': 'GMT+07:00'
}

def bot(token):
    medata = requests.post('https://www.veeuapp.com/v1.0/me?access_token='+ token ,headers=head)
    medata2 = requests.get('https://www.veeuapp.com/v1.0/game/power12?access_token=' + token + '&timezone=GMT%2B07%3A00&locale=th_TH',headers=headDATA2).text
    jsondata = json.loads(medata.text)
    if 'user' in jsondata:
        data = jsondata['user']
        print('UserID: ' + data['user_id'])
        print('Name: ' + data['nickname'])
        print('Email: ' + data['email'])
        print('Points: ' + str(json.loads(medata2)['total_points']))
        print('VIP_level: ' + str(json.loads(medata2)['vip_level']))
        while True:
            botdata = requests.post('https://www.veeuapp.com/v1.0/incentive/tasks?access_token=' + token ,data=json.dumps(video),headers=header)
            medata3 = requests.get('https://www.veeuapp.com/v1.0/game/power12?access_token=' + token + '&timezone=GMT%2B07%3A00&locale=th_TH',headers=headDATA2).text
            print(time.strftime('%m/%d/%Y - %H:%M:%S  ') + 'reward: ' + str(json.loads(botdata.text)['task']['reward_point']) + ' ' + 'Points: ' + str(json.loads(medata3)['total_points']) + '  VIP_level: ' + str(json.loads(medata2)['vip_level']))
            for i in range(random.randint(4,10)):
                time.sleep(random.randint(2,7))
                requests.post('https://www.veeuapp.com/v1.0/log?auth_token=' + token ,headers=headlog)
    else:
        print('ERRER: ' + jsondata['message'])

if __name__ == "__main__":
    token = input('Token: ')
    #token = ''
    bot(token)
