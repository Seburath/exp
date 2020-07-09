from celery import Celery
from os import system


app = Celery('tasker',
            broker="pyamqp://guest@cyberhead-rmq//")


@app.task
def start():
    print('main started')
    #system('celery -A tasker beat --loglevel=info --workdir /app/cyberhead/strategies')
    #system('celery -A tasker beat --loglevel=info --workdir /app/cyberhead/brokers')


'''

system('celery -A tasker worker -B --workdir /app/cyberhead/core')

@app.task
def see_you():
    print('Sending task')
    system('python3 /app/cyberhead/strategies/stratmanager.py')
    print('Task send')


app.conf.beat_schedule = {
    "see-you": {
        "task": "tasker.see_you",
        "schedule": 10
    }
}
'''
