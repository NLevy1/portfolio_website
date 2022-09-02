from flask import Flask, render_template, request
from sheets import DataManager

app = Flask(__name__)

data_manager = DataManager()
dict_list = data_manager.get_sheet_data()


@app.route("/")
def get_main_page():
    return render_template("index.html", projects=dict_list)


@app.route("/project/<project_id>")
def get_project(project_id):
    return render_template("project.html",
                           id=str(project_id),
                           projects=dict_list)


if __name__ == "__main__":
    app.run(debug=True)