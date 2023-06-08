import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [981089412, 449235586]
# voronko:981089412
# greb:1112596301
# oleg:449235586

ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASS = str(os.getenv('PGPASS'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASS}@{ip}/{DATABASE}'
