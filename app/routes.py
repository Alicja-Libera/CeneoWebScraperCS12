from Flask import render_template
from app import app 

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/extract")
def index():
    return render_template("extract.html")

@app.route("/product/<product_id>")
def index(product_id):
    return render_template("product.html", product_id=product_id)

@app.route("/charts/<product_id>")
def index():
    return render_template("charts.html")

@app.route("products")
def index():
    return render_template("products.html")

@app.route("/about")
def index():
    return render_template("about.html")

