import os
from mastodon import Mastodon

DEV = True

if DEV:
    mastoAccessToken = os.environ.get('MASTO_ACCESS_TOKEN_DEV')
    mastoApiBase = os.environ.get('MASTO_API_BASE_DEV')
else:
    mastoAccessToken = os.environ.get('MASTO_ACCESS_TOKEN')
    mastoApiBase = os.environ.get('MASTO_API_BASE')

def main():
    m = Mastodon(access_token=mastoAccessToken, api_base_url=mastoApiBase)
    toot = m.toot('''Hello world, we are testing our tooling
    
    https://mastodonpy.readthedocs.io/en/stable/index.html''')
    m.status_favourite(toot)


if __name__ == '__main__':
    main()