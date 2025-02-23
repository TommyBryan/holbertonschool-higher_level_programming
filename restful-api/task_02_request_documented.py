#!/usr/bin/python3
""" This script fetches the posts from the API and prints them. """

# Import the required modules
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
    url = "https://jsonplaceholder.typicode.com/posts"  # API fetching posts
    response = requests.get(url)  # send GET request to the API
    print(f"Status code: {response.status_code}")  # Print the HTTP status code

    if response.status_code == 200:  # Check if request was successful
        posts = response.json()  # Convert the response to JSON
        for post in posts:
            print(post["title"])  # Print the title of each post
    else:
        print("Failed to fetch posts.")  # Print error message if failed

def fetch_and_save_post():
    """
    Fetches posts from the JSONPlaceholder API and saves them to a CSV file.

    This function sends a GET request to the API endpoint, retrieves
    the response and writes the data into a CSV file if the request
    is successful. The CSV file contains the post ID, user ID, title,
    and body of each post.

    Returns:
        None
    """
    url = "https://jsonplaceholder.typicode.com/posts"  # API endpoint for post
    response = requests.get(url)  # send GET request to the API
    print(f"Status code: {response.status_code}")  # Print the HTTP status code

    if response.status_code == 200:  # Check if request was successful
        posts = response.json()  # Convert the response to JSON

        # Write the data to a CSV file
        with open("posts.csv", "w") as file:  # Open a CSV file in write mode
            writer = csv.writer(file)  # Create a CSV writer object
            writer.writerow(["ID", "User ID", "Title", "Body"])  # Write the header row

            for post in posts:
                writer.writerow([post["id"], post["userId"], post["title"], post["body"]])  # Write data row
    else:
        print("Failed to fetch posts.")  # Print error message if request failed
