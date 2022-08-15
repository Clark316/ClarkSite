# First Website

This is a repository for Clarks first website.

## Install

1. `cd python`
2. `mamba env create -f environment.yaml`

## Starting the Webserver and Running Requests

1. run `conda activate clarkenv`
2. run `cd python`. This will put you in the correct folder to run the commands below
3. run `python server.py`. This starts the webserver
4. open a different terminal window, see the screenshot [open_a_second_terminal.png](./open_a_second_terminal.png)
5. run `conda activate clarkenv` in the new terminal
5. run `python example_requests.py` in the new terminal

## Infrastructure

We're using [Tornado Wwebserver](https://www.tornadoweb.org/en/stable/) as the API server

`server.py`: This is the entrypoint to the webserver application. It has different routes and configures the port that the webserver listens on.
`example_requests.py`: This has an example GET and POST request. Run this file to add and retrieve information from the running webserver.
`handlers`: this folder has all of the handler objects used for the webserver.
`handlers/__init__.py`: this handles some python import stuff, don't worry about it.
`handlers/base_handler.py`: some configuration for http server, also don't worry about it.
`handlers/hello_world.py`: this is your first handler, it defines GET and POST functions. The GET function allows you to get information from the database, POST allows you to add information to the database.

## Git workflow

Add changes to github
```
git add .
git commit -m 'put a message here'
git status
git push
```