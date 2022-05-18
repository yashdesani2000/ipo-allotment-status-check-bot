
from telegram.ext import *
import requests
import pandas as pd

def yash(text):
    ab = ['PAN','APPLNO','DPCLID']
    for a in range(len(ab)):
        try:
            url = 'https://linkintime.co.in/mipo/IPO.aspx/SearchOnPan'
            data={'clientid': '11610',
                    'PAN': text,
                    'key_word': ab[a]
                    }
            s = requests.Session()
            res = s.post(url=url,json=data).text.split('\\')

            Allotment = []

            list = []
            
            for i in range(len(res)):
                    try:
                            
                        if res[i] == 'u003ccompanyname':
                            a = i+1
                            list.append(a)
                        if res[i] == 'u003cNAME1':
                            b=i+1
                            list.append(b)
                        if res[i] == 'u003cDPCLITID':
                            c=i+1
                            list.append(c)
                        if res[i] == 'u003cSHARES' :
                            d=i+1
                            list.append(d) 
                        if res[i] == 'u003coffer_price':
                            e=i+1
                            list.append(e)
                        if res[i] == 'u003cALLOT' :
                            f=i+1
                            list.append(f) 
                        if res[i] == 'u003cAMTADJ' :
                            g=i+1
                            list.append(g)           
                    except:
                        pass

                # print(list)

            for l in list:
                    a = res[l].strip('u003e')
                    Allotment.append(a)
            
            fram = pd.DataFrame(Allotment)
            name = ['Cutoff_price =>','DP_Clint_id =>','Name =>','Company =>','Securities_Allotted =>','Securities_applied =>','Amount_Adjusted =>']
            frm = pd.DataFrame(name)
            dt = pd.concat([frm,fram],axis=1)
            dt.columns=['','']
            if Allotment[4]==Allotment[5]:
                return '''Congretulations You have got Allotment''' , dt
            else:
                return '''Sorry you haven't got Allotment''', dt
        except:
            pass
     
def handle_message(update,context):
        message = update.message.text.upper()
        # print(u)
        if yash(message)==None and message not in ['HI', 'HII', 'HIII']:
            update.message.reply_text('Please enter valid credentials')
        elif yash(message)!=None:    
            update.message.reply_text(str(yash(message)))    
        if message in ['HI', 'HII', 'HIII']:
            update.message.reply_text('Please enter Pan number or Application id or DPID to check Ipo Allotment Status') 



def error(update, context):
    print(f"Update {update} caused error {context.error}")        
       

def main():
    updater = Updater('5317123296:AAE7U6qJdnkhL19_AZfKiDWuq-752j0VGe8', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main() 
