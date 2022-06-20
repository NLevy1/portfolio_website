import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.json_variable_keys = {
            "type": os.getenv("TYPE"),
            "project_id": os.getenv("PROJECT_ID"),
            "private_key_id": os.getenv("PRIVATE_KEY_ID"),
            "private_key": os.getenv("PRIVATE_KEY").replace('\\n', '\n'),
            "client_email": os.getenv("CLIENT_EMAIL"),
            "client_id": os.getenv("CLIENT_ID"),
            "auth_uri": os.getenv("AUTH_URI"),
            "token_uri": os.getenv("TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
            "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL")
        }
        self.scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_dict(self.json_variable_keys, self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("Portfolio Projects").sheet1
        self.data = self.sheet.get_all_records()

    def get_sheet_data(self):
        return self.data
