#!/usr/bin/python3
""" This script fetches the posts from the API and prints them. """

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches post from the JSONPlaceholder API and prints their titles.

    This function sends a GET request to the API endpoint,
    retrieves the response, and prints the titles of all
    the posts if the request is successful.

    Returns:
        None
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """
    Fetches posts from the JSONPlaceholder API and saves them to a CSV file.

    This function sends a GET request to the API endpoint, retrieves
    the response and writes the data into a CSV file if the request
    is successful. The CSV file contains the post ID, user ID, title,
    and body of each post.

    Returns:
        None
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        with open("posts.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "title", "body"])

            for post in posts:
                writer.writerow([post["id"], post["title"], post["body"]])
    else:
        print("Failed to fetch posts.")
