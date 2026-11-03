

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "36702430"))
	API_HASH = os.environ.get("API_HASH", "1e73c1d30b95186ab9866e001cc74603")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "8887348980:AAG4mlMEWfGmUC_ryojgaJbA2QivxCMDN3Y")
	UR_CHANNEL = os.environ.get("UR_CHANNEL", "-1003440366081")
	UR_GROUP = os.environ.get("UR_GROUP", "@fireaimbot1")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "@aimbot_files_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1003982311578"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "7634552382"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sabbir123rok_db_user:kCwZlLyv62GKYYsl@cluster0.ovwarlw.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1003440366081")
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003440366081"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	HOME_TEXT = os.environ.get("HOME_TEXT")
