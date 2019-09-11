from filters.average_tweets_per_day_filter_file import  get_average_tweets_per_day, average_tweets_per_day_filter


bot = {'screen_name': 'TestUserBot', 'id': 10000000000, 'urls': [{'url': 'www.texsaspost.com', 'expanded_url': 'https://texsaspost.com/', 'display_url': 'texsaspost.com', 'indices': [70, 93]}], 'verified': False, 'protected': False, 'created_at': 'Sun Sep 1 16:07:52 +0000 2019', 'statuses_count': 30745, 'description': 'Official account for global news, trends & analysis from the radio team behind World Business Report, Business Matters, Business Daily & Marketplace'}
notbot = {'screen_name': 'TestUserNotBot', 'id': 10000000001, 'urls': [{'url': 'https://bbc.co.uk', 'expanded_url': 'https://bbc.co.uk', 'display_url': 'bbc.co.uk', 'indices': [74, 97]}], 'verified': True, 'protected': False, 'created_at': 'Sun Sep 1 10:18:15 +0000 2019', 'statuses_count': 51, 'description': 'For the latest updates on breaking news visit our website: https://t.co/5os3efxRyQ'}

def test_average_tweets_per_day():
    total = get_average_tweets_per_day(bot)
    assert total == 3074.5
    result = get_average_tweets_per_day(notbot)
    assert result == 5.1


def test_average_tweets_per_day_filter():
     average = average_tweets_per_day_filter(bot)
     assert average == True
     average_notbot = average_tweets_per_day_filter(notbot)
     assert average_notbot == False