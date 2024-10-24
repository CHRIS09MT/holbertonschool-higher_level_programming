import requests, csv, json

def fetch_and_print_posts():
    
    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = resp.json()
    
    print(f"Status Code: {resp.status_code}")
    
    for post in posts:
        print(f"{post['title']}")
        
def fetch_and_save_posts():
    
    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = resp.json()
    
    data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
    
    with open('posts.csv', 'w', newline='') as csvfile:
        fieldname = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames= fieldname)

        writer.writeheader()
        writer.writerows(data)