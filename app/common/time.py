from datetime import datetime,timezone,timedelta

def now():
    return datetime.now(timezone.utc)

# def now_for_SQLite():
    # return int(datetime.now(timezone.utc).timestamp())

# print(type(now()))
# print(now_for_SQLite())
# dt = datetime.fromisoformat(str(now())) -------------
# expired_at = datetime.fromisoformat(row["expired_at"]) #------------- untuk mengembalikan ke tipe data datetime 
# print(type(dt))