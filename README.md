# Gauge with Python and Selenium

This project serves as an example for writing Automation using [Gauge](https://github.com/getgauge/gauge)

This project uses

- [Selenium](http://selenium-python.readthedocs.org/)

# Concepts covered

- ...

# Prerequisites
- Python latest
- Django latest
- [Install Gauge](https://docs.gauge.org/latest/installation.html)

- [Install Gauge-Python plugin](https://gauge-python.readthedocs.io/en/latest/installation.html) by running<br>
```
gauge install python
[pip / pip3] install getgauge
```
- Google Chrome

## Setting up and runing Django app
```
python manage runserver
```

* Open django app with url [http://localhost:8000/](http://localhost:8000)


# Executing specs

### Set up
This project requires pip to install dependencies. To install dependencies run :
````
pip install -r requirements.txt
````


### All specs
````
gauge run specs
````
This will also compile all the supporting code implementations.