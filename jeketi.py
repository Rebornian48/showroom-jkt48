import requests
import datetime
import matplotlib.pyplot as plt
import numpy as np

def search_item(list, product):
    for i in range(len(list)):
        if list[i] == product:
            return True
    return False

list_members=["OFC","Shani","Gracia","Feni","Sisca","Gita","Jesslyn","Eli","Chika","Olla","Zee","Muthe","Christy","Jessi","Freya","Fiony","Oniel","Lulu","Flora","Adel","Kathrina","Ashel","Marsha","Indah","Lyn","Lia","Indira","Amanda","Callie","Ella","Raisha","Cynthia","Daisy","Danella","Anindya","Gracie","Greesel","Alya","Jeane","Michie","Elin","Chelsea","Cathy","Gendhis"]
list_id=[332503,318207,318208,317738,317739,318117,318229,318118,318209,318222,317727,318204,318112,318228,318225,318223,318218,318232,318224,318239,318230,318210,318233,318227,400717,400713,400716,400710,400714,400715,400718,461463,461465,461466,461452,416478,416479,461451,461480,461481,461475,461458,461454,461476]

print('Selamat Datang di Bot Rebornian48 - Showroom JKT48')
print('Di sini akan menampilkan data terkait showroom member JKT48')
print('Silakan input "list" untuk menampilkan data terkait kata kunci, serta input "nama member" yang terdapat pada kunci untuk menampilkan data terkait showroom member JKT48')
x = input()
if search_item(list_members, x):
    num = list_id[list_members.index(x)]
    api_url = "https://www.showroom-live.com/api/room/profile?room_id="+str(num)

    response = requests.get(api_url)
    res = response.json()
    print(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    if res['is_onlive']==True:
        if res['premium_room_type']==1:
            pre="premium"
        print(str(res['room_name']) + " saat ini sedang live " + pre)
        print('Live saat ini dimulai dari ' + str(datetime.datetime.fromtimestamp(res['current_live_started_at']).strftime("%d %b %Y %H:%M:%S")))
        print ('Jumlah Penonton ' + res['room_name'] + ' saat ini : ' + f"{res['view_num']:,d}")
    else:
        print(str(res['room_name']) + " saat ini offline")
        print ('Ranking Kumulatif pada ' + res['room_name'])
        live_api_url = "https://www.showroom-live.com/api/live/summary_ranking?room_id="+str(num)
        res2 = requests.get(live_api_url)
        resp2 = res2.json()
        print(res2.status_code)
        response2 = resp2['ranking']
        i = 0
        list_name = []
        list_point = []
        while i < len(response2):
            print(str(response2[i]['order']) + '. ' + response2[i]['name'] + ' dengan poin ' + f"{response2[i]['point']:,d}")
            list_name.append(response2[i]['name'])
            list_point.append(response2[i]['point'])
            i += 1

        x = np.array(list_name)
        y = np.array(list_point)

        plt.title("Penonton " + str(res['room_name']), loc = 'center')
        plt.xlabel("Poin")
        plt.barh(x,y)

        for i, v in enumerate(y):
            plt.text(v + 1, i, str(v), color='blue', va='center')

        plt.show()
    print(' ')
    print('Saat ini jumlah follower ' + res['room_name'] + ' sebanyak ' + f"{res['follower_num']:,d}")
if x=="list":
    for y in list_members:
        print(y)
else:
    print("Member yang bernama " + x + " tidak ditemukan!")