#from redis_cache import retrieve_users

def bot_bio_filter(user_id):
  bot = ['iamabot', 'imabot', 'justabot']

  # description has whitespace removed and downcased
  bot_bio = ''.join(user['description'].split()).lower()

  if any(x in bot_bio for x in bot):
    return True #print("Bot")
  else:
    return False #print("Not bot")

# def test_filter():
#  users = retrieve_users()
#  res = {}
#  for user in users:
#    res[user['id']] = bot_bio_filter(user['id'])
#
#  print(res)
