import datetime

from workproject.celery1 import app
from telegram.client import send_message
from frauds.models.fraud import Fraud
from google_sheets.client import write_to_sheet


@app.task(bind=True)
def fraud_created_task(self, fraud_name):
    fraud = Fraud.objects.get(numEO=fraud_name)

    message = f"Fraud num {fraud_name}"
    message += f" від {fraud.date}, відділ {fraud.district}"

    write_to_sheet([f"{fraud.numEO}", f"{fraud.date}", f"{fraud.district}"])
    send_message(message)


@app.task(bind=True)
def static_task(self):
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    frauds_one_day = Fraud.objects.filter(date__gt=date_from).count()

    message = f"{frauds_one_day} frauds created today!"
    print(message)
