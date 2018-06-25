import requests
import getpass

username=input("Enter your roll number: ").strip()

password=getpass.getpass("Enter your MIS password: ")

url="https://delta.nitt.edu/results/results.php"

payload={"uname":username, "pwd":password}

headers={"Content-Type":"application/x-www-form-urlencoded"}

session=requests.session()
r=session.post(url, data=payload, headers=headers)

output=r.text[5:len(r.text)-6]

print(output)
