import requests
import os

response = requests.get(
    'http://httpbin.org/get')
print("---Headers---")
print(response.headers)
print("---Header Server---")
print(response.headers['Server'])
print("---Text---")
print(response.text)
print("---Status Code---")
print(response.status_code)

(print("---Params---"))
response = requests.get(
    'http://httpbin.org/get',
    params={'id':1})
print(response.url)

print("---json---")
response = requests.get(
    'http://httpbin.org/get',
    params={'id':3},
    headers={'Accept': 'application/json'})
print(response.text)

print("---delete---")
response = requests.delete(
    'http://httpbin.org/delete')
print(response.text)

print("---post---")
response = requests.post(
    'http://httpbin.org/post',
    data={'key':'value'})
print(response.text)

try:
    files = {'file': open('google.png', 'rb')}
    response = requests.post(
        'http://httpbin.org/post',
        files=files)
    print(response.text)
except Exception as exception:
    print(f"An error occurred: {exception}")

print("---auth---")
response = requests.get(
    'http://httpbin.org/get',
    auth=('user', 'passwd'))
print(response.text)

print("---badssl---")
response = requests.get(
    'https://expired.badssl.com/',
    verify=False)
print(response.text)

print("---Allow Redirects False---")
response = requests.get(
    'http://github.com',
    allow_redirects=False)
print(response.headers)

print("---Timeout---")
try:
    response = requests.get(
        'http://httpbin.org/get',
        timeout=0.01)
    print(response.text)
except requests.exceptions.Timeout:
    print("The request timed out")

print("---Session---")
response = requests.get(
    'http://httpbin.org/cookies',
    cookies={'cookie':'value'})
print(response.text)
response = requests.Session()
response.cookies.update({'cookie':'value'})
print(response.get('http://httpbin.org/cookies').text)
print(response.get('http://httpbin.org/cookies').text)

print("---JSON---")
response = requests.get(
    'https://api.github.com/events')
print(response.json())

print("---Download Image---")
response = requests.get(
    'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    verify=False)
with open('google.png', 'wb') as file:
    file.write(response.content)
if os.path.exists('google.png'):
    print('google.png exists')
os.remove('google.png')