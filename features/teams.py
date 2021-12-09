
from config import *

@bot.message_handler(
    func=lambda message: message.content_type == 'text'
    and ( 
        bool(re.search(r'Team$', message.text, re.IGNORECASE))
         or  bool(re.search(r'Squadra$', message.text, re.IGNORECASE))
        )
)
def team(message):
        user_id = message.from_user.id
        fcx_user = db.User.get_user(user_id)
        lang = fcx_user.language
        bot_info = bot.get_me()
        bot_name = bot_info.username
        withdrawal_minimum_amount = 0.002
        text_info = {
                "en": f"""
Invitation link to share with your friends:
https://t.me/{bot_name}?start={user_id}
        """,
        "it": f"""
Link di invito da condividere con i Vostri amici:
https://t.me/{bot_name}?start={user_id}

        """
        }
        
        text_refferal = {
        "en": """
Refferal system:
1. Level 4%
2. Level 2%
3. Level 1%


Total team earnings:
xx.xxxxxx BTT
        """,
        "it": """
Livelli Bonus:
1. Livello 4%
2. Livello 2%
3. Livello 1%


Guadagno totale della squadra:
xx.xxxxxx BTT
        """
        }
        text_enter_commission = {
        "en": """
Your commissions will be added automatically to your main account balance each time a team member makes a deposit or a reinvestment.
        """,
        "it": """
Le Vostre commissioni saranno aggiunte automaticamente al saldo del Vostro conto principale ogni volta che un membro del team effettua un deposito o un reinvestimento. 
        """
        }
        dashboard[lang].keyboard[0][0] = f"Balances  {fcx_user.account_balance} BTT"
        bot.send_message(
                user_id,
                text=text_info[lang] + text_refferal[lang] + text_enter_commission[lang],
                reply_markup=dashboard.get(lang),
                parse_mode="html"
                )

