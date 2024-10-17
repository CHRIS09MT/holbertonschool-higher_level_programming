import requests
import csv

"""
Fetches posts from an API and prints or saves them as CSV.
"""


def fetch_and_print_posts():
    """Fetches posts from an API and prints their titles."""

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()

    print(f"Status Code: {response.status_code}")

    for post in posts:
        print(f"{post['title']}")


def fetch_and_save_posts():
    """Fetches posts from an API and saves them to a CSV file."""

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()

    data = [
        {"id": post["id"], "title": post["title"], "body": post["body"]}
        for post in posts
    ]

    with open("posts.csv", "w", newline="") as csvfile:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)
