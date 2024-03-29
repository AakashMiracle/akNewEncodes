import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "10811400")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "191bf5ae7a6c39771e7b13cf4ffd1279") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6497663588:AAFcb9_eYNwSCm9shcPf5JO3X8FhBC85mDY") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'Sunrises24BotUpdates') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://PUBLICFILESTORE24BOT:PUBLICFILESTORE24BOT@cluster0.2l9nxfl.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","Cluster0") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6469754522")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001973961950')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/5d0e09278a78ea7c517f4.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Encoded Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
