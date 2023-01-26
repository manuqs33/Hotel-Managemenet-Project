# Hotel Management project

This project is a Django REST API that manages Booking operations for a Hotel.

## Docker and database

The API is built on a Docker container with a docker-compose file to run it. It uses a Sqlite
database, mainly because it's automatically set by Django. For a production-ready API, a more robust alternative, such as PostgreSQL, would be advisable. This would require setting up an additional service and volume in the docker-compose.yaml file.

## Running the project

To run the project in a Docker container, create a virtual env, run `pip install -r requirements.txt`, and run `docker-compose up`. We've set some useful commands in a Makefile, which work automatically in any Linux or MacOS system (if you have a Windows system and want to use the Makefile, search the internet for options to make it available). If the Makefile is available, simply use the `make` command to run the project, and check for other important commands listed there. Some of them require an activated virtualenv to work. If you want to check the database and make some changes, you can access it from the Django admin (http://0.0.0.0:8000/admin) after creating a superuser (check the appropriate command in the Makefile if you don't know it).

## Endpoints

For this API, we've set two Models with their corresponding serializers and Viewsets: Rooms and Bookings. Rooms are designed to be created and destroyed only by an Admin (superuser), while Bookings are designed to be created and updated also from the Front End, probably through an HTML form. Only the Admin, however, has permission to destroy.

For Rooms, we've set two endpoints with a GET method:
- GET http://0.0.0.0:8000/rooms/
Lists all Rooms.
- GET http://0.0.0.0:8000/rooms/{id}/
Retrieves a Room by id.

The goal of these methods is to send information to be shown in the Front End, so the user can choose a Room and make a reservation.

For Bookings, we've set 2 endpoints, each with two available HTTP methods:

- GET http://0.0.0.0:8000/bookings/
Lists all Bookings.
- POST http://0.0.0.0:8000/bookings/
Creates a new Booking.

<br>

- GET http://0.0.0.0:8000/bookings/{id}/
Retrieves a Booking by id.
- PUT http://0.0.0.0:8000/bookings/{id}/
Updates a Booking by id.

Bookings have to be associated with an already existing Room.
Changes in the payment status can be enacted through the update function. We've set three booking statuses: Paid, Pending, and Deleted. A partial_update function corresponding to a PATCH HTTP method could also have been set, but we avoided it for simplicity's sake. In the Front End, an autofill for the Booking fields should be added, so the user could change only those he needs to update.
Also, Rooms' price Field is meant to be calculated automatically in the Front End from the room's price and the number of days the Booking lasts. In this case, an additional server-side validation could be useful to prevent attacks, but we have not included one yet. As such, to test the API, it must be filled manually in the requests to the proper endpoint. Also, Bookings currently include clients' information in their Fields. In a large application that wanted to store information about them in the database, a separate Client model could be set.


## Validation and Postman

We've added a few validations to make the API more logically consistent. Of course, a production-ready API would probably include more validation methods, and we plan to include some more in the future.

1) The first one validates that the end_date of a reservation is posterior to its start_date.
2) The second one validates that a new or updated reservation doesn't overlap with the reservation period of another one, unless it has a Deleted status.

Finally, we've included a Postman file with some examples related to the endpoints and validations.
