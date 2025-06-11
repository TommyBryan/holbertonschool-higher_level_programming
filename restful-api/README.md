# RESTful API Learning Project

## Introduction
In the evolving world of software development, understanding how to communicate and transfer data efficiently between systems is essential. This project delves into the domain of RESTful APIs, a cornerstone in the realm of web services. The Representational State Transfer (REST) architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.

## Learning Objectives
- **HTTP/HTTPS Basics**: Understand how data transfer occurs, the methods involved, and the difference between secure and non-secure versions.
- **API Consumption with Command Line**: Gain hands-on experience in interacting with APIs using command-line tools.
- **API Consumption with Python**: Learn to fetch and manipulate data using Python.
- **API Development with `http.server`**: Develop a foundational understanding of crafting APIs with Python’s built-in modules.
- **API Development with Flask**: Explore API development using the Flask framework.
- **API Security & Authentication**: Learn how to protect data and ensure secure access.
- **API Standards & Documentation with OpenAPI**: Maintain standardized documentation for usability and maintainability.

## Importance
RESTful APIs are crucial in modern digital communication. They facilitate data exchange between systems, making them an essential component of applications ranging from social media platforms to industrial automation. Understanding how to consume, develop, secure, and document these APIs provides a valuable skill set for software development.

## REST API Conceptual Diagram
```
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database
```
### Components:
- **Client**: Sends a request (e.g., web browser or application).
- **Web Server**: Receives and forwards the request.
- **API Server**: Processes the request and interacts with the database.
- **Database**: Stores and retrieves data as needed.

### Flow:
1. The client sends an HTTP/HTTPS request.
2. The Web Server forwards the request to the API Server.
3. The API Server processes the request and interacts with the database.
4. The API Server returns the response to the Web Server.
5. The Web Server sends the final response to the client.

## Tasks
### 0. Basics of HTTP/HTTPS
#### Background
HTTP is the foundation of web communication, while HTTPS provides an added layer of security using SSL/TLS encryption.

#### Objective
- Differentiate between HTTP and HTTPS.
- Understand HTTP request and response structures.
- Learn common HTTP methods and status codes.

#### Instructions
1. Read about HTTP and HTTPS differences.
2. Inspect network requests using browser developer tools.
3. List common HTTP methods and status codes with their use cases.

#### Expected Output
- Summary of HTTP vs HTTPS differences.
- Outline of HTTP request/response structure.
- List of common HTTP methods and status codes with explanations.

### 1. Consume Data from an API Using Command Line Tools (curl)
#### Background
`curl` is a command-line tool for data transfer over networks. It is useful for interacting with RESTful APIs.

#### Objective
- Install and use `curl`.
- Construct API requests using `curl`.
- Interpret API responses.

#### Instructions
1. Install `curl` and verify installation with `curl --version`.
2. Fetch webpage content: `curl http://example.com`
3. Retrieve API data: `curl https://jsonplaceholder.typicode.com/posts`
4. Fetch only headers: `curl -I https://jsonplaceholder.typicode.com/posts`
5. Make a POST request: `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`

#### Expected Output
- Verification of `curl` installation.
- JSON output of posts from JSONPlaceholder.
- HTTP headers from API response.
- Response acknowledging POST request data submission.

---
This project provides a hands-on approach to understanding and working with RESTful APIs, enhancing both theoretical knowledge and practical skills.

