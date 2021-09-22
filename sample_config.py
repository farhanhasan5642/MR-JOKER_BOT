# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/mrjoker/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 8245524  # integer value, dont use ""
    API_HASH = "b4ee2d8b7c4cb8fff5a572a0ff75bb19"
    TOKEN = "2036142327:AAG00iVk9jsH67zocfDhu-ZRfGI1drWJURY"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1935084498  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Farhan5642"
    SUPPORT_CHAT = "ogsssssw"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001366894756
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001366894756
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://txxbkmyxgmqztv:e63ef7f0b9d6c0628637312acfc1ead8d85bf8c7114b2f4723e17d03be4fc369@ec2-23-20-208-173.compute-1.amazonaws.com:5432/dbn7mpu6qromu1"  # needed for any database modules
    REDIS_URI = " "
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "mIlwjtmjVrZhtMpO8K7IDPqZZwqWFfIM5~gIqEOFeNbkRWkRP3nAlFndMhuCCa6Y"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = "1935084498"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "1935084498"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "1935084498"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "1935084498"
    WOLVES = "1935084498"
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "14ZRNHX7RG6F4274"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "VYJUP5VELGXW"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "hmm"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "hmmm"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
