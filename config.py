import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "24314944")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "608c07ba57d9130d9974c9b3639ec570") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6463184992:AAEGu_OXXXWpnKIyop0L4WHwepvSddstRJg") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'Opleech') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://sessiongenerator:sessiongenerator@cluster0.zsejhr4.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","WOODEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6264350806")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001774386816')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/15e82d7e665eccc8bd9c5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""