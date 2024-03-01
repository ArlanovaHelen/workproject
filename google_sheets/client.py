import gspread
import os

CREDENTIALS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "credentials.json"
)

gc = gspread.service_account(filename=CREDENTIALS_PATH)


def write_to_sheet(data):
    sh = gc.open("Frauds")
    worksheet = sh.sheet1

    worksheet.append_row(data)
