# Bot token provided by BotFather

from sqlalchemy import create_engine


# PUBLIC_KEY = "80343df2dff487a2499ac6b2fc7d832d0b80cb4566107f6a03d4404e5b289b4e"
# PRIVATE_KEY = "4672CFA54E54975177E5A2ae5a44e125c3687d9cdF15606Da96c2ba49B994037"
# Merchant_ID = "7a52533349195fd518a34ffd446c8a0a"
# IPN_secret = "btttradingexpress"
# ADMIN_ID = 1355336561

DEBUG = not True

if DEBUG==False:
    print("\033[1;35;40m Running in production mode")
    TOKEN = "5086018821:AAGjDVmpp-bMK4MbSxjmgBAAP9VNFcceO-E" #BTT Trading Express
    URL = 'https://btt-trading-express.herokuapp.com/'
    try:
        import os
        DATABASE_URL = os.environ['DATABASE_URL']
    except KeyError:
        # DATABASE_URL="postgres://ijmhoygudgmxru:49370293052dcaf5a977de733a4cb129f0f6a001f2a64da604fc4a4b5927af7e@ec2-44-193-111-218.compute-1.amazonaws.com:5432/d822275vn10alp"
        DATABASE_URL="postgres://ijmhoygudgmxru:49370293052dcaf5a977de733a4cb129f0f6a001f2a64da604fc4a4b5927af7e@ec2-44-193-111-218.compute-1.amazonaws.com:5432/d822275vn10alp"
    db_url = DATABASE_URL.split(":")

    DATABASE_URI_VAR =f'postgres+psycopg2:{db_url[1]}:{db_url[2]}:{db_url[3]}'
    engine = create_engine(DATABASE_URI_VAR, echo=True)
    print(engine)

else:
    print("\033[1;32;40m Running in Development mode")
    TOKEN = "5086018821:AAGjDVmpp-bMK4MbSxjmgBAAP9VNFcceO-E"

    URL = "https://3a7a746b.ngrok.io/"
    DATABASE_URL = 'postgres+psycopg2://postgres:postgres@localhost:5432'
    ADMIN_ID = 1053579181

    SQLITE = 'sqlite:///database/database.db'
    engine = create_engine(SQLITE, echo=True, connect_args={'check_same_thread': False})
    print(engine)

