DRF Project

a simple django rest api endpoints

A user will be able to get a list of all the contacts and will be able to create a new contact using a endpoint.
A user will be able to update and delete a contact a endpoint

Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Installation

First create a Virtual environmnet using following command
  python3 -m venv myenv

Clone the project to your local machine using following command
  git clone https://github.com/nazmul49/DRFProject.git

Run the program using following command
  python manage.py runserver

Now Open your browser and enter
  127.0.0.1:8000(port can be different depending on your server port)

Check the Endpoints

http://127.0.0.1:8000/api/v1/contact/ - A user will be able to get a list of all the contacts and will be able to create a new contact using this endpoint.
http://127.0.0.1:8000/api/v1/contact/id/ - A user will be able to update and delete a contact using this endpoint.