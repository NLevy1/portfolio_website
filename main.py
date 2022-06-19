from flask import Flask, render_template, request
from sheets import DataManager
import requests

app = Flask(__name__)

data_manager = DataManager()
dict_list = data_manager.get_sheet_data()


@app.route("/")
def get_main_page():
    return render_template("index.html", projects=dict_list)


@app.route("/project/<id>")
def get_project(id):
    return render_template("project.html",
                           id=str(id),
                           projects=dict_list)

@app.route("/all_projects")
def get_all_projects():
    return render_template("all_projects.html",
                           projects=dict_list)


if __name__ == "__main__":
    app.run(debug=True)
