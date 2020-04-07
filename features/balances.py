
from config import *

@bot.message_handler(
    func=lambda message: message.content_type == 'text'
    and (
        bool(re.search(r'^balance[s.]', message.text.split()[0], re.IGNORECASE)) or 
        bool(re.search(r'^bilance', message.text.split()[0], re.IGNORECASE))
        )
)
def balance(message):
    """Returns account balance report"""
    
    chat_id = message.chat.id
    user_object = get_user(message)
    if user_object["lang"] not in ["ENGLISH", "ITALIAN"]:
        show_language(message)
    else:
        lang = user_object["lang"]

        try:
            balance = user_object["investment"]['balance']
            active_investment = user_object["investment"]['active_investment']
            active_reinvestment = user_object["investment"]['active_reinvestment']
            pending_investment = user_object["investment"]['pending_investment']
            
            
            balance_text = {

            "ENGLISH": f"""


Your Account Balance:
<strong>{balance} BTC</strong>
Total Active Investments:
<strong>{active_investment} BTC</strong>
Total Active Reinvestments:
<strong>{active_reinvestment} BTC</strong>
Total Pending Investments:
<strong>{pending_investment} BTC</strong>

Base rate: 0.2% per day.
You may add another investment by pressing the <strong>DEPOSIT</strong> button. Your Balance will be grow up according Base rate and your Referrals.
            """,

            "ITALIAN": f"""


Saldo del conto:
<strong>{balance} BTC</strong>
Investimenti attivi:
<strong>{active_investment} BTC</strong>
Reinvestimenti attivi:
<strong>{active_reinvestment} BTC</strong>
Investimenti in sospeso:
<strong>{pending_investment} BTC</strong>

Tariffa base: 0,2% al giorno.
È possibile aggiungere un altro investimento premendo il pulsante <strong>DEPOSIT</strong>. Il tuo saldo crescerà in base alla tariffa base e ai tuoi referral.        


 """
            }
            bot.send_message(chat_id, text=balance_text[lang], reply_markup=dashboard.get(lang), parse_mode="html")
        except KeyError:
            no_balance_text = {
                "ENGLISH": f"""
                    No investment yet. Go to <b>Deposit</b> to add funds.
                """,
                "ITALIAN": f"""
                    Ancora nessun investimento. Andate a Deposito per aggiungere fondi.
                """
                }
            bot.send_message( chat_id, text=no_balance_text[lang], reply_markup=dashboard.get(lang), parse_mode="html")