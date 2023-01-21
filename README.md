# Hotel Management project

This project is a Django-Rest API to manage the Booking operations for a Hotel.

## Docker and database

The API is built on a Docker container with a docker-compose file to run it. It has a Sqlite
database, as it is mainly an exercise. For a production-ready API, a more robust alternative,
such as PostgreSQL, would be advisable. This would require setting up an additional service
and volume in docker-compose.yaml

## Running the project

To run the project from a container, create a virtual env, run `pip install /r requirements.txt`,
and run `make` or `docker-compose up`. We've set some commands in a Makefile to help the user run some commands. Many of them require an activated virtualenv. Creating a superuser may be advisable if checking the admin panel would be necessary.

## Endpoints

For this app, we've set two Models with their corresponding serializers and viewsets: Rooms and Bookings. Rooms are designed to be created and destroyed only by the Admin, while Bookings are designed to be created and updates from the Front End, probably from an HTML form. Only the Admin, however, has destroying privileges.

For Rooms, we've set two endpoints:
1) GET http://0.0.0.0:8000/rooms/
This is a list method for all Rooms.
2) GET http://0.0.0.0:8000/rooms/id/
This retrieves a Room by id.

The goal of these method is to send information to be shown in the Front End, so the user can choose a Room and make a reservation.

For Bookings, we've set  endpoints:
1) GET http://0.0.0.0:8000/bookings/
This is a list method for all Bookings.
2) GET http://0.0.0.0:8000/bookings/id/
This retrieves a Booking by id.
3) POST http://0.0.0.0:8000/bookings/
This creates a new Booking
4) PUT http://0.0.0.0:8000/bookings/id/
This updates a Booking by id.

Bookings have to be associated to an already existing Room.
The update can be used to update payment status. We've set three booking statuses: Payed, Pending, and Deleted. A partial_update method corresponding to PATCH could also have been set, but we avoided it for simplicity's sake. In the Front End, an autofill for the Booking fields, so the user could change only those he needs to update.
Also, the price Field is meant to be calculated automatically in the Front End from the room's price and the number of days the Booking includes. In this case, an additional server-side validation could be useful to prevent attacks, but for the purposes of this demonstration it must be filled manually in the requests. Also, Bookings currently include clients' information. In a large aplication that wanted to store information about them in the database, a separate Client model could be set.


## Validation and Postman

Although additional validation besides the one performed by Django-Rest serializers wasn't mentioned as a requirement, we've added two to experiment and make the API more logically consistent. Of course, a production-ready API would probably include more validation methods. The two we've set are:

1) The first one validates that the end_date of a reservation is posterior to its start_date.
2) The second one validates that a new or updated reservation doesn't overlap with the reservation period of another one, unless it has a Deleted status.

Finally, we've included a Postman file with some examples related to the endpoints in validations.
