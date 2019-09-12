from filters.retweet_count_filter import  retweet_ratio_filter, retweet_count


bot = {'screen_name': 'TestUserBot', 'id': 10000000000,'user_id': 10000000000,'urls': [{'url': 'www.texsaspost.com', 'expanded_url': 'https://texsaspost.com/', 'display_url': 'texsaspost.com', 'indices': [70, 93]}], 'tweeted_status': 220, 'verified': False, 'protected': False, 'created_at': 'Sun Sep 1 16:07:52 +0000 2019', 'statuses_count': 30745, 'description': 'imabot Official account for global news, trends & analysis from the radio team behind World Business Report, Business Matters, Business Daily & Marketplace'}
notbot = {'screen_name': 'TestUserNotBot', 'id': 10000000001, 'user_id': 10000000001, 'urls': [{'url': 'https://bbc.co.uk', 'expanded_url': 'https://bbc.co.uk', 'display_url': 'bbc.co.uk', 'indices': [74, 97]}], 'tweeted_status': 220, 'verified': True, 'protected': True, 'created_at': 'Sun Sep 1 10:18:15 +0000 2019', 'statuses_count': 51, 'description': 'For the latest updates on breaking news visit our website: https://t.co/5os3efxRyQ'}

def test_retweet_ratio_filter():
    user = retweet_ratio_filter(bot,200)
    assert user == True

