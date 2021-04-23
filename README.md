Hi Matthew ,A thousand apologies for the delay, the truth is that I have very little time I tried to do everything, I don't know if I told you Mercedes but I am moving to London. .


I couldn't get my hands on it until two days ago that I stayed awake ahaha. (surely many things with more lucidity I do them better)

Well I would be very interested in working with you, the truth is, the interviews are very cool.
Keep growing in both machine learnig Terraform and kubernetes, and whatever comes next,

# Considerations I had:

* I assumed that the doctor had the office at latitude 0 and longitude 0. (to get the distance, I calculate the vector) distance ^ 2 = longitude ^ 2 + latitude ^ 2.

* The first filter is the attendance ratio, second filter is the distance, third the time of atendance

Add:
- Deploy, pipeline with Github actions
- Docker-compose
- Docker- File
- Two types of databases, (sqlLite, psql)

With more time :
- Deliver a back office to manage the office.
- I would improve the tests (I would do them again well)
- I would put more emphasis on the ML algorithm (just for the sake of learning, this weekend I'm sure to think about it)


  

Whatever happens, thanks for the good vibes.


# Python Engineer Take Home Project

The goal of this exercise is to demonstrate your problem solving skills.
There is no "right" answer.

# Problem Statement

A busy doctor's office needs a way to figure out what patients they
should see first based on how many appointments they've shown up for,
missed, average time the appointment takes, and the distance to the
office.

# Requirements

* Confirm to PEP-8.
* Model the json data structure using [pydantic](https://pydantic-docs.helpmanual.io).
* Implement an HTTP REST API using
  [FastAPI](https://fastapi.tiangolo.com) with the following endpoints:
  * Get a single patient by id (GET /patients/:id)
  * Get the next patient that has the high attendance to missed ratio
    (GET /patients/next).
  * Register a new patient (POST /patients).
  * Delete an existing patient (DELETE /patients/:id).
* Dockerize application.
* Use `pytest` for testing.
* Create utility class(es) so that in the future, logic can be reused.

# Deliverables

* Run the application with a single `docker-compose up`
* Ability to test the API using swagger (built-in with FastAPI).

# Bonus

Want to take it to the next level? Feel free to sprinkle in some of your
ninja skills! Here are some ideas:

* Implement a database technology like MySQL or PostgreSQL.
* Use some fancy ML to determine probability.
* Create a UML.
* Submit a PR to make this test better!
