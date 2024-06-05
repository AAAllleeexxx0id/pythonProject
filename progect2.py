import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('FinalProgect.html')

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    dish = request.form.get('dish')
    drink = request.form.get('drink')

    conn = sqlite3.connect('restaurant.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO orderss (name, dish, drink) VALUES (?, ?, ?)',
                   (name, dish, drink))
    conn.commit()
    conn.close()

    return 'Order added successfully!'

app.run(debug=True)



# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <link rel="stylesheet" href="static/styles.css" type="text/css">
#     <title>Flask Form</title>
# </head>
# <body>
#     <h1 class="hhhhh1">Restaurant flask</h1>
#     <hr>
#     <h3>Enter your name down here: </h3>
#     <form action="/add" method="post">
#         <div>
#             <input type="text" name="name">
#         </div>
#         <h3>Choose dish: </h3>
#         <select class="lst1" name="dish">
#             <option>soup</option>
#             <option>borscht</option>
#             <option>potatoes with cutlets</option>
#             <option>cabbage rolls</option>
#             <option>french fries</option>
#             <option>burger</option>
#         </select>
#         <h3>Choose drink: </h3>
#         <select id="drink" name="drink">
#             <option>coffe(latte)</option>
#             <option>coffe(Americano)</option>
#             <option>coffe(Glasse)</option>
#             <option>tea(Green)</option>
#             <option>tea(White)</option>
#             <option>tea(Black)</option>
#             <option>lemonade(Berry)</option>
#             <option>lemonade(Coconut)</option>
#             <option>lemonade(Tropical)</option>
#             <option>cocktail(Mojito)</option>
#             <option>cocktail(Bumblebee)</option>
#             <option>cocktail(Classic)</option>
#             <option>martini(Rosato)</option>
#             <option>martini(Bianco)</option>
#             <option>martini(Fiero)</option>
#             <option>beer(Brown Ale)</option>
#             <option>beer(Porter)</option>
#             <option>beer(Stout)</option>
#         </select>
#         <button type="submit">Add</button>
#     </form>
#     </hr>
# </body>
# </html>



# body {
#     background-color: #FF9933;
# }
# .hhhhh1 {
#     width: 900px;
#     height: 30px;
#     color: #c00;
#     font-size: 30px;
#     font-family: 'Tahoma';
#     margin-left: 650px;
# }