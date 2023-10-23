import datetime
from telethon import TelegramClient, Button, events
import os
from random import randint

api_id = #тут вводимо ID бота
api_idl = #а тут хеш якщо я не помиляюся

target_can = 1488171183 # Вводимо id в який будемо пересилати повідомлення
target_cant = 748451671 



now = datetime.datetime.now().time()
day = datetime.datetime.today().weekday()

para1 = datetime.datetime.strptime('9 00', '%H %M').time()
para1end = datetime.datetime.strptime('10 20', '%H %M').time()
para2 = datetime.datetime.strptime('10 30', '%H %M').time()
para2end = datetime.datetime.strptime('12 00', '%H %M').time()
para3 = datetime.datetime.strptime('12 10', '%H %M').time()
para3end = datetime.datetime.strptime('13 30', '%H %M').time()
para4 = datetime.datetime.strptime('13 40', '%H %M').time()
para4end = datetime.datetime.strptime('15 00', '%H %M').time()

kwt = ["/test",'/test@sho_po_pare_bot']
kwf = ['/furry','фуррі','/furry@sho_po_pare_bot']
kwp = ["що по парі?", "яка пара?", "SPP", "/para","/para@sho_po_pare_bot"]

lol_answer = 'відпочиває...'


randphoto=102
path_to_furry = r"C:\Users\Taras\code\SPP BOT 2\SPP2_py\.furry"
path_to_nsfw_furry = r"C:\Users\Taras\code\SPP BOT 2\SPP2_py\.furry\furri_nsffw"
photoGalary = []
photoGalary = os.listdir(path_to_furry)
print(photoGalary)
photoGalary = [r"C:/Users/Taras/code/SPP BOT 2/SPP2_py/.furry/"+f for f in photoGalary]
#print('after add path: '+photoGalary[randphoto])

linkslist = ['', 'Англ - Хуянгил: https://us04web.zoom.us/j/74330820901?pwd=aTLcTTruTrX7l8zYHbLWGYYtOIHBb3.1', 'Фізра: https://us05web.zoom.us/j/9932278470?pwd=M0loWDJDNEZzOGFCTkhpNXZac1JVZz09', 'Природничі: https://us04web.zoom.us/j/72515098402?pwd=QBMbCOUdFgXCov8MxWJTNgYlcpb4ii.1', 'Математика: https://us04web.zoom.us/j/74101045238?pwd=PWnBQzofmarCiyDEGOa2YGt0tmlrWB.1', 'Укр мова і літ: https://us05web.zoom.us/j/89738925786?pwd=UFY3cFZJeWlvNXpoSzFXVXkzV1JIUT09', 'Креслення: https://us04web.zoom.us/j/74206849969?pwd=RmPbioa2vWYEhfknSBBFFZE7VViLYf.1', 'Механіка: https://meet.google.com/mmu-ezfi-zar', 'Теорія підзалупних кіл та сигналів: https://us04web.zoom.us/j/74908827031?pwd=SDgw7WQzO2aaXmpTFrxm81gYZcDKOB.1', 'Оптика: https://us04web.zoom.us/j/76852237298?pwd=mtVwHQcR9EqBbVfY1BQTIdlGlBepw5.1','Основи метрології: https://us05web.zoom.us/j/83868371347?pwd=eStpajJMWVI1dHMwc0VOL25WUVJndz09',"ІКГ: https://us05web.zoom.us/j/86270523804?pwd=bWWYRD4GyhLZdLEVazducI3FCmPEdC.1",'Електротехніка: :https://us05web.zoom.us/j/82794836081?pwd=Nzc2UUdmN1liRFU1K3lyR04wYjZGQT09','Технологія оптичного приладобудування та обробки оптичних деталей: https://us05web.zoom.us/j/82724689041?pwd=cGZVRERaaWJFSDkremFBa3dvdEV4Zz09','Тепловізійні пристрої та системи: https://us05web.zoom.us/j/93073438525?pwd=K2ExblNiOFVVYjREV2pJZ0FPM0lFQT09', lol_answer]
#у списку 14 елементів тобто від 0 до 13
#0-"" 1-Англ, 2-Фізра, 3-Природничі, 4-Математика, 5-Укр мова і літ, 6-Креслення, 7-Механіка, 
#8-Теорія підзалупних кіл та сигналів, 9-Оптика, 10-Основи метрології 11-ІКГ 12-електроніка 
#13-Технологія оптичного приладобудування 14-Тепловізійні пристрої та системи 
#15- пішов нахуй
bot = TelegramClient("Test", api_id, api_idl).start(bot_token='5970307940:AAG4GhFnsnhGSA2tM4Oa5G8apse-jXH8620')
linktopara=['pisun']
nowWeek = 1

#target_can=bot.get_entity(1488171183)
#target_cant=bot.get_entity(748451671)

def randphotom():
    randphoto = randint(0, len(photoGalary)-1)
    return randphoto

def paraonlyW1(nomer, altRozcladWeek1, rozcladWeek1):
    if altRozcladWeek1[nomer] != 0:
        linktopara.append("МНТ:\n"+linkslist[rozcladWeek1[nomer]]+"\n\nЕТ:\n"+linkslist[altRozcladWeek1[nomer]])
    else:
        linktopara.append("МНТ/ЕТ:\n"+linkslist[rozcladWeek1[nomer]])
def paraonlyW2(nomer, altRozcladWeek2, rozcladWeek2):
    if altRozcladWeek2[nomer] != 0:
        print("and link: ", linkslist[altRozcladWeek2[nomer]])
        linktopara.append("МНТ:\n"+linkslist[rozcladWeek2[nomer]]+"\n\nЕТ:\n"+linkslist[altRozcladWeek2[nomer]])
    else:
        linktopara.append("МНТ/ЕТ:\n"+linkslist[rozcladWeek2[nomer]])

def para_check(rozcladWeek1, altRozcladWeek1, rozcladWeek2=[] , altRozcladWeek2=[]):
    now = datetime.datetime.now().time()
    print('now: ', now)
    linktopara.clear()
    if nowWeek == 1:
        if now >= para1 and now <= para1end:
            print('para 2', ', link:', linkslist[rozcladWeek1[0]])
            paraonlyW1(0, altRozcladWeek1, rozcladWeek1)
        elif now >= para2 and now <= para2end:
            print('para 2', ', link:', linkslist[rozcladWeek1[1]])
            paraonlyW1(1, altRozcladWeek1, rozcladWeek1)
        elif now >= para3 and now <= para3end:
            print('para 3', ', link:', linkslist[rozcladWeek1[2]])
            paraonlyW1(2, altRozcladWeek1, rozcladWeek1)
        elif now >= para4 and now <= para4end:
            print('para 4', ', link:', linkslist[rozcladWeek1[3]])
            paraonlyW1(3, altRozcladWeek1, rozcladWeek1)
        elif now >= para4end:
            print('para 5', ', link:', linkslist[rozcladWeek1[4]])
            paraonlyW1(4, altRozcladWeek1, rozcladWeek1)
        else:
            print('no para')
            paraonlyW1(4, altRozcladWeek1, rozcladWeek1)
    else:
        pass 
        #тут повинен бути блок з розкладом на другий тиждень але він не горить тому похуй покищо 

@bot.on(events.NewMessage())
async def normal_handler(event):
    if event.message.message in kwp:
            if day == 0:
                para_check([11,1,9,9,15], [0,0,0,0,0])
                await bot.send_message(target_can, linktopara[0])
            elif day == 1:
                para_check([15,11,9,9,15], [0,0,0,0,0])
                await bot.send_message(target_can, linktopara[0])
            elif day == 2:
                para_check([13,13,9,15,15], [0,0,0,0,0])
                await bot.send_message(target_can, linktopara[0])
            elif day == 3:
                para_check([13,13,2,15,15], [0,0,0,0,0])
                await bot.send_message(target_can, linktopara[0])
            elif day == 4:
                para_check([14,9,9,15,15], [0,0,0,0,0])
                await bot.send_message(target_can, linktopara[0])
            else:
                print('no para, weekend')
                await bot.send_message(target_can, 'no para, weekend')
        
    elif event.message.message in kwf:
        randphoto = randint(0, len(photoGalary)-1)
        print('furry working, maybe')
        await bot.send_message( target_can,'', file=[photoGalary[randphotom()], photoGalary[randphotom()], photoGalary[randphotom()]], silent=True )
#"незнав що ти таким цікавишся, ну загалом не моя справа"
    elif event.message.message in kwt:
        bot.parse_mode = 'html'
        await bot.send_message(target_can, "нових фіч зараз в розробці немає, бо я не придумав чогсь геніального, якщо у ваз зявилася цікава думка, але ну от прям геніальна то звертаййтеся до <a href="">Неваляшки</a>... потім дороблю, та і типу ви все одно знаєте хто мене пише!")


bot.start()
bot.run_until_disconnected()
