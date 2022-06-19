# Bot token provided by BotFather
TOKEN = "5519479434:AAE719MsOPWSlu26ASt4o1IdMGvKrwT4T3g"
from sqlalchemy import create_engine


PUBLIC_KEY = "b244d10593047726ba5e9d28618e0ccb8011b0e3d5fa46ebc7fa06a3bddea76b"
PRIVATE_KEY = "b339ffefdc3Ca98e05C118c96ABFd04b41eb1f000Ea38767B8Dc618d9765a3D7"
MERCHANT_ID = "7be647419765bcca807fa020a62c03d0"
IPN_secret = "Myinves"
ADMIN_ID = 551129540

DEBUG = not True

if DEBUG==False:
    print("\033[1;35;40m Running in production mode")
    TOKEN = "5519479434:AAE719MsOPWSlu26ASt4o1IdMGvKrwT4T3g" #BTT Trading Express
    URL = 'https://myinvespace.herokuapp.com//'
    try:
        import os
        DATABASE_URL = os.environ['DATABASE_URL']
    except KeyError:
        # DATABASE_URL="postgres://ijmhoygudgmxru:49370293052dcaf5a977de733a4cb129f0f6a001f2a64da604fc4a4b5927af7e@ec2-44-193-111-218.compute-1.amazonaws.com:5432/d822275vn10alp"
        DATABASE_URL="postgres://ioegvgkzxmrtzw:c5455b70226ed75ec6a2d82f91c75c1ab3eb46c01ff4550a7d1fcd0ad9b817c0@ec2-52-204-195-41.compute-1.amazonaws.com:5432/d7j9dqto5av2ej"
    db_url = DATABASE_URL.split(":")

    DATABASE_URI_VAR =f'postgres+psycopg2:{db_url[1]}:{db_url[2]}:{db_url[3]}'
    engine = create_engine(DATABASE_URI_VAR, echo=True)
    print(engine)

else:
    print("\033[1;32;40m Running in Development mode")
    TOKEN = "5519479434:AAE719MsOPWSlu26ASt4o1IdMGvKrwT4T3g"

    URL = "https://3a7a746b.ngrok.io/"
    DATABASE_URL = 'postgres://ioegvgkzxmrtzw:c5455b70226ed75ec6a2d82f91c75c1ab3eb46c01ff4550a7d1fcd0ad9b817c0@ec2-52-204-195-41.compute-1.amazonaws.com:5432/d7j9dqto5av2ej'
    ADMIN_ID = 1053579181

    SQLITE = 'sqlite:///database/database.db'
    engine = create_engine(SQLITE, echo=True, connect_args={'check_same_thread': False})
    print(engine)

