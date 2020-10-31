# Check Post is about Pankaj Or Not.

post=input("Enter The Post :\n")
post=post.lower()

if('pankaj' in post):
    print('Pankaj , This post for you.')
else:
    print('Pankaj , This post not for you.')