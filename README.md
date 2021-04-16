# Python Engineer Take Home Project

The goal of this exercise is to demonstrate your problem solving skills.
There is no "right" answer.

# Problem Statement

A busy doctor's office needs a way to figure out what patients they
should see first based on how many appointments they've shown up for,
missed, average time the appointment takes, and the distance to the
office.

# Requirements

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
