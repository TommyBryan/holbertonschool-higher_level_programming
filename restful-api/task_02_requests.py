#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"  # Placeholder API URL
    response = requests.get(url)  # Make a GET request to the API
    print(f"Status Code: {response.status_code}")  # Prints status code
    """ 
    If the request was sucessfull, parse the fetched data into a JSON object using the .json() method
    of the response object. Iterate through the parsed JSON data and print out the titles of all the posts.
    """
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Title: {post['title']}")
    if response.status_code != 200:
        print("Failed to fetch posts.")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"  # Placeholder API URL 
    response = requests.get(url)  # Make a GET request to the API
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        
        # Create a new list with only id, title, and body
        post_data = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(post_data)

        print("Posts saved to posts.csv")
    else:
        print("Failed to fetch posts.")
