from flask import Flask, request
index_app_counter=0
app = Flask("ayonsAplication")
counter = 0

@app.route('/')
def helloWorld():
    global index_app_counter
    index_app_counter += 1
    return "Hello World"

@app.route('/hello/<name>')
def hello_name(name):
   return f"Hello {name}!"


@app.route("/blog")
def blog():
    global index_app_counter
    index_app_counter += 1
    return "This is a new blog"

@app.route("/counter")
def showCounter():
    global index_app_counter
    counter = str(index_app_counter)
    return f"""
        <html>
            <head>
                <style>
                    body{{
                        color:#00008b;
                        font-size: 300%;
                        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
                    }}
                </style>
            </head>
            <body>
                <div>
                    {counter}
                </div>
            </body>
        </html>
    """

@app.route('/form')
def sendDataFromHtmlForm():
    return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <style>
                    body{{
                        color:#00008b;
                        font-size: 100%;
                        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
                    }}
                </style>
            </head>
            <body>
                <div>
                    <h1>The input form attribute</h1>

                    <p>The form attribute specifies the form an input element belongs to.</p>

                    <form action="/processForm" id="form1">
                        <label for="fname">First name:</label>
                        <input type="text" id="fname" name="fname"><br><br>
                        <input type="submit" value="Submit">
                    </form>

                    <p>The "Last name" field below is outside the form element, but still part of the form.</p>

                    <label for="lname">Last name:</label>
                    <input type="text" id="lname" name="lname" form="form1">
                </div>
            </body>
        </html>
    """


@app.route('/processForm', methods=['POST', 'GET'])
def showDataFromHtmlForm():
    if request.method == 'GET':
        firstName = request.args.get('fname')
        lastName = request.args.get('lname')
        return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <style>
                    body{{
                        color:#00008b;
                        font-size: 100%;
                        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
                    }}
                </style>
            </head>
            <body>
                <div>
                    Welcome {lastName}{firstName}, welcome to web development.
                </div>
            </body>
        </html>
        """


if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug = True)