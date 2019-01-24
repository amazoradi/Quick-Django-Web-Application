# Quick Django Web Application

## Instructions

You are going to build your own Django powered web application. It will be very similar to what we built during the Django tutorial walkthrough.

### Project Setup

1. Create a Django [project](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#creating-a-project) named `music`.
1. Create a [new application](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#creating-the-polls-app) in your project named `history`.
1. In `history/urls.py`, define a route for listing artists, and one for show a specific artist's details.

### Models

1. Build a [model](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#creating-models) representing your `Artist` table.
1. Build a [model](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#creating-models) representing your `Song` table. Ensure that you define the foreign key to the artist table.

### Views

1. Define a [view](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#writing-more-views) to return a [template](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#use-the-template-system) that lists all artists.
1. Define a [view](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#writing-more-views) to return a [template](https://docs.djangoproject.com/en/2.0/intro/tutorial03/#use-the-template-system) that displays the details of a specific artist, and list all of the songs related to that artist.

### Migrations

Remember that every time you create a model, or update it, you need to [create a migration](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#activating-models), and run it.

### Populate Database

1. Create a SQL script at the root of your project, where the database file is located. 
1. Open the database in your DB Browser
1. Paste your SQL script into DB Browser's Execute SQL window and run it
1. You can use insert statements kinda like this:
`INSERT into Artist
values (null, "The Kinks", 1964)` 
to insert data into your `Artist` and `Song` tables 


# Optional Stretch Goals

1. Style your templates with CSS by setting up your application to serve static files.
1. Create a site template for your music history that both the artist list, and the artist detail templates extend.
