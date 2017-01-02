import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    week_ago = datetime.strftime(datetime.now() - timedelta(days=7), '%Y-%m-%d')
    url = 'https://api.github.com/search/repositories'
    payload = {'q': 'created:>%s' % week_ago, 'sort': 'stars', 'per_page': top_size}
    response = requests.get(url, params=payload)
    return response.json()["items"]


def print_repositories(data):
    for i, repository in enumerate(data):
        print('%s) Repository "%s"' % (i + 1, repository['name']),
              'has %s stars, %s open issues' % (repository['stargazers_count'], repository['open_issues']),
              'and located here: %s' % repository['html_url'])


if __name__ == '__main__':
    repositories_quantity = 20
    print_repositories(get_trending_repositories(repositories_quantity))
