import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size, days_ago):
    start_date = datetime.strftime(datetime.now() - timedelta(days=days_ago), '%Y-%m-%d')
    url = 'https://api.github.com/search/repositories'
    payload = {'q': 'created:>%s' % start_date, 'sort': 'stars', 'per_page': top_size}
    response = requests.get(url, params=payload)
    return response.json()["items"]


def print_repositories(data):
    for number, repository in enumerate(data, start=1):
        print('%s) Repository "%s"' % (number, repository['name']),
              'has %s stars, %s open issues' % (repository['stargazers_count'], repository['open_issues']),
              'and located here: %s' % repository['html_url'])


if __name__ == '__main__':
    repositories_quantity = 20
    period_of_days = 7
    print_repositories(get_trending_repositories(repositories_quantity, period_of_days))
