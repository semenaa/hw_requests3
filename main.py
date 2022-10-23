import requests
import datetime



class stackOverflowReader:
    def __init__(self, token: str):
        self.token = token

    # Принимает кол-во дней и тэг вопроса
    def get_questions(self, days: int, tag: str):
        self.url = 'https://api.stackexchange.com/2.3/questions'

        presentDate = datetime.datetime.now()
        unix_todate = int(datetime.datetime.timestamp(presentDate))
        unix_fromdate = unix_todate - (days * 24 * 60 * 60)
        self.params = {
            'fromdate': str(unix_fromdate),
            'todate': str(unix_todate),
            'order': 'desc',
            'sort': 'creation',
            'tagged': tag.lower(),
            'site': 'stackoverflow'
        }
        return requests.get(url=self.url, params=self.params).json()


if __name__ == '__main__':
    token = ''
    q = stackOverflowReader(token)
    for question in q.get_questions(2, 'Python')['items']:
        print(question['title'])