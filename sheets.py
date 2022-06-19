import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.json_variable_keys = {
            "type": os.environ.get("type"),
            "project_id": os.environ.get("project_id"),
            "private_key_id": os.environ.get("private_key_id"),
            "private_key": os.environ.get("private_key"),
            "client_email": os.environ.get("client_email"),
            "client_id": os.environ.get("client_id"),
            "auth_uri": os.environ.get("auth_uri"),
            "token_uri": os.environ.get("token_uri"),
            "auth_provider_x509_cert_url": os.environ.get("auth_provider_x509_cert_url"),
            "client_x509_cert_url": os.environ.get("client_x509_cert_url")
        }
        self.scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_dict(self.json_variable_keys, self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("Portfolio Projects").sheet1
        self.data = self.sheet.get_all_records()

    def get_sheet_data(self):
        return self.data
