
from flask import Flask, request
from flask_cors import CORS
import boto3, os
from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
load_dotenv()

UPLOAD_FOLDER = 'D:/Coding/PythonProgramming/fullStack/back-end/static/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'js'}


os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'


app = Flask("testApplication")
CORS(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['S3_BUCKET'] = os.getenv('S3_BUCKET') 
app.config['S3_KEY'] = os.getenv('S3_KEY') 
app.config['S3_SECRET'] = os.getenv('S3_SECRET') 
app.config['S3_LOCATION'] = os.getenv('S3_LOCATION') 

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('S3_KEY') ,
    aws_secret_access_key=os.getenv('S3_SECRET')
)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return "My name is Rakib! (came from server)"


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
        # print(request.files['selectedFile'])
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

    
@app.route("/get-buckets")
def getBuckets():
    bucketsObject = s3.list_buckets()
    buckets = {}
    bucketNumber = 1
    for bucketObject in bucketsObject["Buckets"]:
        buckets[f"bucket{bucketNumber}"] = bucketObject["Name"]
        bucketNumber += 1
    return buckets


@app.route("/create-bucket")
def createBucket():
    try:
        my_session = boto3.session.Session()
        my_region = my_session.region_name
        print("region: ",my_region)
        # region = "us-east-1"
        # location = {'LocationConstraint': region}
        buckets = getBuckets()
        for bucketName in buckets.values():
            if bucketName == "flask-bucket-of-asdtoyihjerdoiuj":
                return "bucket already exists!"
        s3.create_bucket(Bucket="flask-bucket-of-asdtoyihjerdoiuj")
        # Bucket names are GLOBALLY unique! AWS CLI will give you the IllegalLocationConstraintException 
        # if you collide with an already existing bucket and you've specified a region different than the region of the already existing bucket. 
        # If you happen to guess the correct region of the existing bucket it will give you the BucketAlreadyExists exception.
    except ClientError as e:
        print(e)
        return "Could not connect to S3"
    return "created bucket!"
    


@app.route("/get-files")
def getFiles():
    fileObjects = s3.list_objects(Bucket="ayonbucket")['Contents']
    fileNames = {}
    fileNumber = 1
    for fileObject in fileObjects:
        key = f"file number{fileNumber}"
        fileNames[key] = fileObject["Key"]
        fileNumber += 1
    return fileNames


@app.route("/download-file", methods = ["POST"])
def downloadFile():
    if request.method == "POST":
        data = request.get_json()
        files = getFiles()
        fileName = data["name"]
        for fileNameInS3 in files.values():
            if fileNameInS3 == fileName:
                s3 = boto3.resource('s3', aws_access_key_id=os.getenv('S3_KEY') , aws_secret_access_key=os.getenv('S3_SECRET'))
                s3.Bucket("ayonbucket").download_file(f"{fileName}", f"D:/Coding/PythonProgramming/fullStack/back-end/static/files/downloaded-from-s3/{fileName}")
                return "file was downloaded!"
        return "file was not found!"
        

@app.route("/search-files", methods = ["POST"])
def searchFile():
    if request.method == "POST":
        data = request.get_json()
        print("data is: ",data)
        files = getFiles()
        # print("files in search files url are: ",files)
        matchedFileNames = {}
        fileNumber = 1
        for fileName in files.values():
            modifiedFileName = fileName[0:fileName.find(".")]
            if data['name'] in modifiedFileName:
                matchedFileNames[f"file{fileNumber}"] = fileName
                fileNumber += 1
        return matchedFileNames


if __name__ == "__main__":
    app.debug = True
    app.run()