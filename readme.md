# Django Blog Application

This is a simple blog application built with Django and Django REST Framework.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository_url>

    Install dependencies:

    bash

1. Install dependencies:
    > CMD   pip install -r requirements.txt



2.  Apply database migrations:
    > CMD python manage.py migrate


3.  Run the development server:
    > CMD python manange.py runserver



## API Endpoints
    ### Authentication

        Obtain Token: POST /api/token/
            Request Body:
            json

        {
            "username": "example_user",
            "password": "your_password"
        }


        ### Response:

        json

        {
            "access": "your_access_token",
            "refresh": "your_refresh_token"
        }


    ### Refresh Token: POST /api/token/refresh/

        Request Body:
        json

        {
            "refresh": "your_refresh_token"
        }

        Response:

        json

        {
            "access": "your_new_access_token"
        }


## Posts

    List Posts: GET /api/posts/

    ### Create Post: POST /api/posts/
        Request Body:
        json

        {
        "title": "New Post Title",
        "content": "Post content goes here"
        }

        Response:

        json

            {
            "id": 1,
            "title": "New Post Title",
            "content": "Post content goes here",
            "author": "example_user",
            "published_date": "2024-04-10T12:00:00Z"
            }

        Retrieve Post: GET /api/posts/{post_id}/

        Update Post: PUT /api/posts/{post_id}/

            Request Body:

            json

            {
            "title": "Updated Post Title",
            "content": "Updated content goes here"
            }

        Delete Post: DELETE /api/posts/{post_id}/


## Comments

    ### List Comments for Post: GET /api/posts/{post_id}/comments/

    ### Create Comment for Post: POST /api/posts/{post_id}/comments/
        Request Body:

        json

        {
            "text": "This is a new comment"
        }

        Response:
        json

        {
            "id": 1,
            "post": 1,
            "author": "example_user",
            "text": "This is a new comment",
            "created_date": "2024-04-10T12:00:00Z"
        }



In this README file:

- **Setup Instructions** section provides step-by-step instructions on how to set up and run the application.
- **API Endpoints** section documents all available API endpoints along with example requests and responses.

Make sure to replace placeholder values like `your_access_token`, `your_refresh_token`, `example_user`, etc., with actual values from your application. Update the endpoints and examples as needed based on your project implementation.
