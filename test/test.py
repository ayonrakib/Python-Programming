import base64
import random

urlInString = "[\"ZlbnRyeS4xOTU0MDUwMzA0PW1laGphYmluZXZhLmNlQGdtYWls\",\"aW5ldmEuY2UlNDBnbWFpbC5jb20tQmxKekxKRnlJSXk3cVpVSy\",\"LmNvbQ==\",\"50cnkuMTAxMzkwOTE1PWdXYUEzamVJdUNFcGlwZHgtbWVoamFi\",\"lwUUxTZS1nQUx1eFBKanJPVEZ2MnpCX0FSQVFBbEtGRHlYdTVS\",\"b2xHcGxablNvLUw2akFBL3ZpZXdmb3JtP3VzcD1wcF91cmwmZW\",\"aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQU\"]"
urlInList = ["ZlbnRyeS4xOTU0MDUwMzA0PW1laGphYmluZXZhLmNlQGdtYWls","aW5ldmEuY2UlNDBnbWFpbC5jb20tQmxKekxKRnlJSXk3cVpVSy","LmNvbQ==","50cnkuMTAxMzkwOTE1PWdXYUEzamVJdUNFcGlwZHgtbWVoamFi","lwUUxTZS1nQUx1eFBKanJPVEZ2MnpCX0FSQVFBbEtGRHlYdTVS","b2xHcGxablNvLUw2akFBL3ZpZXdmb3JtP3VzcD1wcF91cmwmZW","aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQU"]
# for element in urlInList:
#     print(element)
#     print(base64.b64decode(element))

# print(base64.b64decode("aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQU"))


firstDecodedUrl = "ZlbnRyeS4xOTU0MDUwMzA0PW1laGphYmluZXZhLmNlQGdtYWls"
secondDecodedUrl = "aW5ldmEuY2UlNDBnbWFpbC5jb20tQmxKekxKRnlJSXk3cVpVSy"
thirdDecodedUrl = "50cnkuMTAxMzkwOTE1PWdXYUEzamVJdUNFcGlwZHgtbWVoamFi"
fourthDecodedUrl = "aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQU"
fifthDecodedUrl = "LmNvbQ=="
urls = [firstDecodedUrl, secondDecodedUrl, thirdDecodedUrl, fourthDecodedUrl, fifthDecodedUrl]

# print(base64.b64decode(fourthDecodedUrl + firstDecodedUrl+  secondDecodedUrl +thirdDecodedUrl   ))

# secondUrl = "aW5ldmEuY2UlNDBnbWFpbC5jb20tQmxKekxKRnlJSXk3cVpVSy" = b'ineva.ce%40gmail.com-BlJzLJFyIIy7qZUK
# fourthDecodedUrl = "aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQU" = https://docs.google.com/forms/d/e/1FAF
# fifthDecodedUrl = "LmNvbQ==" = .com
# .try.101390915=gWaA3jeIuCEpipdx-mehjab.com

# finalurl = ""
# appendedStrings = []
# number = 0
# while(len(appendedStrings) < 5):
#     print("loop number: ")
#     currentEncodedUrl = random.choice(urls)
#     if currentEncodedUrl not in finalurl:
#         finalurl += random.choice(urls)
#         appendedStrings.append(random.choice(urls))
# print(finalurl)
# print(base64.b64decode(firstDecodedUrl))
# print(base64.b64decode(secondDecodedUrl))
# print(base64.b64decode(thirdDecodedUrl))
# print(base64.b64decode(fourthDecodedUrl))
print(base64.b64decode(fifthDecodedUrl))