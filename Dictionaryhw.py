n1 = {}

n1["1xx"] = "the request was received, continuing process"
n1["2xx"] = "the request was successfully received, understood, and accepted"
n1["3xx"] = "further action needs to be taken in order to complete the request"
n1["4xx"] = "the request contains bad syntax or cannot be fulfilled"
n1["5xx"] = "the server failed to fulfil an apparently valid request"
code=input("Enter an error code.")
print(n1[code])