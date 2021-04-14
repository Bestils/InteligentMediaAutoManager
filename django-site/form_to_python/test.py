import sys

login = sys.argv[1]
password = sys.argv[2]

output = "Hello %s! How are You ? Your password is %s" % (login, password)
print(output)