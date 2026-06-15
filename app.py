from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        with open("volunteers.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, email, phone])

    return render_template("index.html")

@app.route("/volunteers")
def volunteers():

    data = []

    with open("volunteers.csv", "r") as file:
        for row in file:
            data.append(row.strip().split(","))

    return render_template("volunteers.html", data=data)

@app.route("/report")
def report():

    with open("volunteers.csv", "r") as file:
        data = file.readlines()

    total = len(data)

    return f"Total Volunteers Registered: {total}"

if __name__ == "__main__":
    app.run(debug=True)