import datetime
from telethon import TelegramClient, events  # Імпортуємо потрібні бібліотеки

api_id = 
api_idl = ""
target_can =  # Вводимо id в який будемо пересилати повідомлення

key_words_test =['що по парі?', 'Що по парі?', 'para']
key_words_test1=['Повітряна тривога в Київській області!']
key_words_test2=['Відбій тривоги в Київській області!']
povitrana_test=0

now = datetime.datetime.now().time()
day = datetime.datetime.today().weekday()

#now = datetime.datetime.strptime('9 20', '%H %M').time()
#day = datetime.datetime.strptime('1', '%w').weekday()

para1 = datetime.datetime.strptime('9 00', '%H %M').time()
para1end = datetime.datetime.strptime('10 20', '%H %M').time()
para2 = datetime.datetime.strptime('10 30', '%H %M').time()
para2end = datetime.datetime.strptime('12 00', '%H %M').time()
para3 = datetime.datetime.strptime('12 10', '%H %M').time()
para3end = datetime.datetime.strptime('13 30', '%H %M').time()
para4 = datetime.datetime.strptime('13 40', '%H %M').time()
para4end = datetime.datetime.strptime('15 00', '%H %M').time()

linkslist = ['Електротехніка: :https://us05web.zoom.us/j/82794836081?pwd=Nzc2UUdmN1liRFU1K3lyR04wYjZGQT09', 'Англ - Хуянгил: https://us04web.zoom.us/j/74330820901?pwd=aTLcTTruTrX7l8zYHbLWGYYtOIHBb3.1', 'Фізра: https://us05web.zoom.us/j/9932278470?pwd=M0loWDJDNEZzOGFCTkhpNXZac1JVZz09', 'Природничі: https://us04web.zoom.us/j/72515098402?pwd=QBMbCOUdFgXCov8MxWJTNgYlcpb4ii.1', 'Математика: https://us04web.zoom.us/j/74101045238?pwd=PWnBQzofmarCiyDEGOa2YGt0tmlrWB.1', 'Укр мова і літ: https://us05web.zoom.us/j/89738925786?pwd=UFY3cFZJeWlvNXpoSzFXVXkzV1JIUT09', 'Креслення: https://us04web.zoom.us/j/74206849969?pwd=RmPbioa2vWYEhfknSBBFFZE7VViLYf.1', 'Механіка: https://meet.google.com/mmu-ezfi-zar', 'Теорія підзалупних кіл та сигналів: https://us04web.zoom.us/j/74908827031?pwd=SDgw7WQzO2aaXmpTFrxm81gYZcDKOB.1', 'Оптика: https://us04web.zoom.us/j/74040504098?pwd=FBbq8ga8whFiQ5oeLCMuN6MXGU6z4E.1','вікно']
#у списку 11 елементів тобто від 0 до 10 
#0-Електротехніка 1-Англ, 2-Фізра, 3-Природничі, 4-Математика, 5-Укр мова і літ, 6-Креслення, 7-Механіка, 8-Теорія підзалупних кіл та сигналів, 9-Оптика, 10-вікно
linktopara = []

def para_check(day, rozklad):
    now = datetime.datetime.now().time()
    print('now: ', now)
    global linktopara
    linktopara.clear()
    if now >= para1 and now <= para1end:
        print(day, ', para 1', ', link:', linkslist[rozklad[0]])
        linktopara.append(linkslist[rozklad[0]])
    elif now >= para2 and now <= para2end:
        print(day, ', para 2', ', link:', linkslist[rozklad[1]])
        linktopara.append(linkslist[rozklad[1]])
    elif now >= para3 and now <= para3end:
        print(day, ', para 3', ', link:', linkslist[rozklad[2]])
        linktopara.append(linkslist[rozklad[2]])
    elif now >= para4 and now <= para4end:
        print(day, ', para 4', ', link:', linkslist[rozklad[3]])
        linktopara.append(linkslist[rozklad[3]])
    else:
        print(day, ', no para')

bot = TelegramClient("Test", api_id, api_idl).start(bot_token='5970307940:AAG4GhFnsnhGSA2tM4Oa5G8apse-jXH8620')
@bot.on(events.NewMessage(chats= [-1001505028797]))
async def normal_handler(event):
    global povitrana_test
    for i1 in range(len(key_words_test1)):
        if key_words_test1[i1] in event.message.message:
            povitrana_test=1
            print('povitrana_test == ', povitrana_test)
        else:
            for i2 in range(len(key_words_test2)):
                if key_words_test2[i2] in event.message.message:
                    povitrana_test=0
                    print('povitrana_test == ', povitrana_test)

@bot.on(events.NewMessage(chats= [1488171183]))
async def normal_handler(event):
    for i in range(len(key_words_test)):
        if key_words_test[i] in event.message.message:
            if day == 0:
                para_check('Monday',[7,9,5,5])
                await bot.send_message(target_can, linktopara[0])
            elif day == 1:
                para_check('Tueasday',[4,2,4,10])
                await bot.send_message(target_can, linktopara[0])
            elif day == 2:
                para_check('Wednesday',[7,9,9,1])
                await bot.send_message(target_can, linktopara[0])
            elif day == 3:
                para_check('Thursday',[10,7,4,8])
                await bot.send_message(target_can, linktopara[0])
            elif day == 4:
                para_check('Friday',[3,6,5,1])
                await bot.send_message(target_can, linktopara[0])
            else:
                print('no para, weekend')
                await bot.send_message(target_can, 'no para, weekend')

        if key_words_test[i] in event.message.message:
            global povitrana_test
            print('pro povitrany')
            print('povitrana_test == ', povitrana_test)
            if povitrana_test == 1:
                await bot.send_message(target_can, 'повітряна є')
                print('повітряна є')          

bot.start()
bot.run_until_disconnected()ц
