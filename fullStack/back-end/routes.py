
from flask import Flask, request
from flask_cors import CORS
import boto3, os
from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'D:/Coding/PythonProgramming/fullStack/back-end/static/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', '.js'}


os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'



app = Flask("testApplication")
CORS(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['S3_BUCKET'] = "ayonbucket"
app.config['S3_KEY'] = "AKIA2AV63QNIZNYTTM4I"
app.config['S3_SECRET'] = "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"
app.config['S3_LOCATION'] = 'arn:aws:s3:::ayonbucket'

s3 = boto3.client(
    's3',
    aws_access_key_id="AKIA2AV63QNIZNYTTM4I",
    aws_secret_access_key="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"
)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return "My name is Rakib!(came from server)"


@app.route("/get-square-of-number", methods = ["POST"])
def getSquare():
    if request.method == "POST":
        number = request.form.get('number')
        print("number in get-square url is: ", number)
        return number
    return 0


@app.route("/upload-file-in-s3", methods=['GET', 'POST'])
def uploadInS3():
    if request.method == 'POST':
        # check if the post request has the file part
        print("arrived in upload-file-in-s3 url")
        print(request.files['selectedFile'])
        if 'selectedFile' not in request.files:
            return "no files!"
        file = request.files['selectedFile']
        print("file is: ",file)
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return "file name is empty"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            print("s3 obj is: ",s3)
            try:
                response = s3.upload_file(UPLOAD_FOLDER + "/" + f"{filename}", "ayonbucket", f"{filename}")
            except ClientError:
                return "could not save in S3!" 
            return "success!"
        else:
            return "file was not saved!"

    

@app.route("/create-bucket")
def createBucket():
    try:
        my_session = boto3.session.Session()
        my_region = my_session.region_name
        print("region: ",my_region)
        # region = "us-east-1"
        # location = {'LocationConstraint': region}
        s3.create_bucket(Bucket="flask-bucket-of-asdtoyihjerdoiuj")
        # Bucket names are GLOBALLY unique! AWS CLI will give you the IllegalLocationConstraintException 
        # if you collide with an already existing bucket and you've specified a region different than the region of the already existing bucket. 
        # If you happen to guess the correct region of the existing bucket it will give you the BucketAlreadyExists exception.
        buckets = s3.list_buckets()
        print("buckets: ",buckets)
    except ClientError as e:
        print(e)
        return "failed to create bucket!"
    return "created bucket!"


if __name__ == "__main__":
    app.debug = True
    app.run()