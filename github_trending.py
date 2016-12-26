import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    date_week_ago = datetime.strftime(datetime.now() - timedelta(days=7), '%Y-%m-%d')
    url = 'https://api.github.com/search/repositories?q=created:>%s&sort=stars&per_page=%d' % (date_week_ago, top_size)
    r = requests.get(url)
    return r.json()["items"]


def print_repositories(data):
    for i, d in enumerate(data):
        print('%s) Repository "%s"' % (i + 1, d['name']),
              'has %s stars, %s open issues' % (d['stargazers_count'], d['open_issues']),
              'and located here: %s' % d['html_url'])


if __name__ == '__main__':
    repo_count = 20
    print_repositories(get_trending_repositories(repo_count))
