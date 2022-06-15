# rbraoit22

Webpage for RBR's Class of 2022 I.T. Academy

## Description

The goal of this project was to introduce others to the bright minds of Red Bank Regional’s Academy of Information Technology’s Class of 2022 and to convey the breadth of our accomplishments in a permanent manner -  the website will persist and be accessible even after we graduate.

The project was constructed using Flask, a Python micro web framework. I chose Flask mostly because I’ve heard great things and wanted to try it for myself. Additionally, it’s very lightweight in comparison to more hefty frameworks such as Django (though both have their different use cases).

This project boasts an impressive onboarding workflow that integrates data collected from Google Forms as well as in-house JSON (JavaScript Object Notation) data files. This essentially makes this website a ‘template’ that can be used for future years (though no class will be quite as special as ours!).

## Running the site

`source venv/bin/activate` to activate virtual environment
Be sure to install dependencies with `pip3 install -r requirements.txt`
`gunicorn --bind 0.0.0.0:5000 run:app` or `gunicorn run:app` to run the flask app
