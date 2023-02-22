from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def item_list():
    items = [
        {'name': 'sauce', 'price': 100},
        {'name': 'rice', 'price': 120},
        {'name': 'carrot', 'price': 70},
        {'name': 'sweet candy', 'price': 50},
    ]
    sort_order = request.args.get('sort_order', 'asc')
    return render_template('Q4.html', items=items, sort_order=sort_order)

if __name__ == '__main__':
    app.run()