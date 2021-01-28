from flask import Flask, send_from_directory, render_template

app = Flask("localServer", static_folder="", static_url_path="/", template_folder="")

@app.route('/')
def homePage():
    return render_template('practice.html')


@app.route('/textfile')
def textFile():
    return send_from_directory('D:/Python Programming/Ajax/text',"sampleText.txt")


if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug=True)