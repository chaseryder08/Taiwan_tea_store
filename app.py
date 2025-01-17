from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'Fafa1928!'

# Sample product data (this can be replaced with a database)
TEAS = [
    {"id": 1, "name": "High Mountain Oolong", "price": 25.00},
    {"id": 2, "name": "Sun Moon Lake Black Tea", "price": 20.00},
    {"id": 3, "name": "Jasmine Green Tea", "price": 15.00}
]

@app.route('/')
def home():
    return render_template('home.html', teas=TEAS)

@app.route('/add_to_cart/<int:tea_id>')
def add_to_cart(tea_id):
    tea = next((t for t in TEAS if t['id'] == tea_id), None)
    if not tea:
        return "Tea not found!", 404

    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append(tea)
    session.modified = True
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/clear_cart')
def clear_cart():
    #clear the cart session data
    session.pop('cart', None)
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Simulate a checkout process
        session.pop('cart', None)  # Clear the cart after checkout
        return "Thank you for your purchase!"

    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
