

from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20366634"))
    API_HASH = getenv("API_HASH", "72095ec36984aa9ceb0dbaa9cec31559")
    BOT_TOKEN = getenv("BOT_TOKEN", "7242758381:AAGkWrJ1z_0Jrmggh-Bo2D_6036Xj92NX4w")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002291875883")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "7845335174").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://rohitreddyathuru:R6Co7MOjTYQOAqcq@cluster0.xrwjpl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

