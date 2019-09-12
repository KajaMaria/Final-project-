from filters.active_hours_per_day_filter import  map_activity_hours, active_hours_per_day_filter


bot = {'screen_name': 'TestUserBot', 'id': 10000000000, 'urls': [{'url': 'www.texsaspost.com', 'expanded_url': 'https://texsaspost.com/', 'display_url': 'texsaspost.com', 'indices': [70, 93]}], 'verified': False, 'protected': False, 'created_at': 'Sun Sep 1 16:07:52 +0000 2019', 'statuses_count': 30745, 'description': 'imabot Official account for global news, trends & analysis from the radio team behind World Business Report, Business Matters, Business Daily & Marketplace'}
notbot = {'screen_name': 'TestUserNotBot', 'id': 10000000001, 'urls': [{'url': 'https://bbc.co.uk', 'expanded_url': 'https://bbc.co.uk', 'display_url': 'bbc.co.uk', 'indices': [74, 97]}], 'verified': True, 'protected': True, 'created_at': 'Sun Sep 1 10:18:15 +0000 2019', 'statuses_count': 51, 'description': 'For the latest updates on breaking news visit our website: https://t.co/5os3efxRyQ'}


# def test_active_hours_per_day_filter():
#     result = active_hours_per_day_filter(bot,start_date=0,end_date=0)
#     assert result == 24

# def test_map_activity_hours():
#     timestamp = test_map_activity_hours(tweets_timestamps)



#   activity_map = {}
#   for timestamp in tweets_timestamps:
#     created_at = convert_timestamp_to_datetime(timestamp)
#     created_at_date = created_at.date()
#     if created_at_date in activity_map:
#       activity_map[created_at_date].add(created_at.hour)
#     else:
#       activity_map[created_at_date] = set([created_at.hour])
#   return activity_map
  