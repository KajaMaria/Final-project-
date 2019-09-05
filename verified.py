from twitterapi import run_twitter_query


def return_non_verified_nonprotected_users():
    results = run_twitter_query()

    users = []

    for user in results:
        if user['verified'] == False and user['protected'] == False:
            users.append(user['screen_name'])
    return users


print(return_non_verified_nonprotected_users())
