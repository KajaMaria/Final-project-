from filters.verified_filter import  unverified_and_unprotected_user_filter


bot = {'screen_name': 'TestUserBot', 'id': 10000000000, 'urls': [{'url': 'www.texsaspost.com', 'expanded_url': 'https://texsaspost.com/', 'display_url': 'texsaspost.com', 'indices': [70, 93]}], 'verified': False, 'protected': False, 'created_at': 'Sun Sep 1 16:07:52 +0000 2019', 'statuses_count': 30745, 'description': 'Official account for global news, trends & analysis from the radio team behind World Business Report, Business Matters, Business Daily & Marketplace'}
notbot = {'screen_name': 'TestUserNotBot', 'id': 10000000001, 'urls': [{'url': 'https://bbc.co.uk', 'expanded_url': 'https://bbc.co.uk', 'display_url': 'bbc.co.uk', 'indices': [74, 97]}], 'verified': True, 'protected': True, 'created_at': 'Sun Sep 1 10:18:15 +0000 2019', 'statuses_count': 51, 'description': 'For the latest updates on breaking news visit our website: https://t.co/5os3efxRyQ'}

def test_unverified_and_unprotected_user_filter():
    total = unverified_and_unprotected_user_filter(notbot)
    assert total == False
    total = unverified_and_unprotected_user_filter(bot)
    assert total == True