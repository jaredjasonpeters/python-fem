import requests

github_api = 'https://api.github.com/search/repositories'


def create_query(languages, min_stars=50000):
    query = f'stars:>{min_stars} '
    for language in languages:
        query += f'language:{language} '
    return query


def getRepos(api, languages, sort='stars', order='desc'):

    query = create_query(languages)

    params = {'q': query, 'sort': sort, 'order': order}

    response = requests.get(api, params=params)

    if(response.status_code == 403):
        raise RuntimeError('Rate limit reached. Please wait and try again')

    if(response.status_code != 200):
        raise RuntimeError(
            f'An error occured. HTTP Status code: {response.status_code}')

    response_json = response.json()

    return response_json['items']


if __name__ == "__main__":
    languages = [
        'javascript',
        'python'
    ]
    results = getRepos(github_api, languages)

    for result in results:
        language = result['language']
        stars = result['stargazers_count']
        name = result['name']

        print(f'-> {name} is a {language} repo with {stars}')
