import requests
import json
import pprint


def get_resource():
    response = requests.get(r'http://jsonplaceholder.typicode.com/users')
    response = response.json()
    result ={}
    for i in response:
       result[i['username']]=i['email']
    pprint.pprint(result)

def create_resorce():
    data = {"1001", "a@b.com"}
    response = requests.post("http://jsonplaceholder.typicode.com/posts", data)
    result =response.json()
    if response.status_code != 201:
        print("Failed create a resouce")
    else:
        print("From the respobse : {}".format(result['id']))

def delete_resource():
    response = requests.delete("http://jsonplaceholder.typicode.com/posts/1")
    if response.status_code != 200:
        print("Fail to delete the resource")

if __name__ == "__main__":
    get_resource()
    create_resorce()
    delete_resource()