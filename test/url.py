import base64
import random
firstDecodedUrl = "ZlbnRyeS4xOTU0MDUwMzA0PW1laGphYmluZXZhLmNlQGdtYWls"
secondDecodedUrl = "aW5ldmEuY2UlNDBnbWFpbC5jb20tQmxKekxKRnlJSXk3cVpVSy"
thirdDecodedUrl = "50cnkuMTAxMzkwOTE1PWdXYUEzamVJdUNFcGlwZHgtbWVoamFi"
fourthDecodedUrl = "aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQU"
fifthDecodedUrl = "LmNvbQ=="

print(base64.b64decode(fourthDecodedUrl+ fifthDecodedUrl+thirdDecodedUrl+ secondDecodedUrl+firstDecodedUrl     ))


# fourthDecodedUrl +firstDecodedUrl  +secondDecodedUrl + thirdDecodedUrl  + fifthDecodedUrl