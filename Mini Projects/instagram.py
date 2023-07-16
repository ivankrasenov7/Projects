import instaloader

bot= instaloader.Instaloader()

profile = instaloader.Profile.from_username(bot.context, 'ivan.krasenov7')

print(type(profile))

print(f"Username: {profile.username}")
print(f"USER ID: {profile.userid}")
print(f"Number of Posts: {profile.mediacount}")
print(f"Followers: {profile.followers}")
print(f"Followees: {profile.followees}")
print(f"Bio: {profile.biography, profile.external_url}")

# followers = [follower.username for follower in profile.get_followers()]
# followees = [followee.username for followee in profile.get_followees()]
# print(followers)

profile = instaloader.Profile.from_username(bot.context, 'ivan.krasenov7')

posts = profile.get_posts()

for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")

