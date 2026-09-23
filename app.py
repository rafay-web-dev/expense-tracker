from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        amount = float(request.form["amount"])

        expenses.append({
            "name": name,
            "amount": amount
        })

    total = sum(expense["amount"] for expense in expenses)

    return render_template(
        "index.html",
        expenses=expenses,
        total=total
    )


@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)