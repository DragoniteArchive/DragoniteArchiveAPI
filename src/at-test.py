import os
from atproto import Client, client_utils

DEV = True

if DEV:
    atUser=os.environ.get('AT_USER_DEV')
    atPass=os.environ.get('AT_PASS_DEV')
else:
    atUser=os.environ.get('AT_USER')
    atPass=os.environ.get('AT_PASS')

def main():
    client = Client()
    profile = client.login(atUser, atPass)
    print('Welcome,', profile.display_name)

    text = client_utils.TextBuilder().text('Hello World, ').link('we are testing our tooling', 'https://atproto.blue')
    post = client.send_post(text)
    client.like(post.uri, post.cid)


if __name__ == '__main__':
    main()