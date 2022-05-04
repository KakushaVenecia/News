# News4U

## Author

Kakusha Venecia 

# Description
* This app will show news articles from several sources and news sources that a user can click to see morw news. The  application gets news from the NEWS API

## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* virtualenv


## Running the Application
* Creating the virtual environment

        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
        $ python3.6 -m pip install Flask-Script

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.8 sources_test.py 
        $ python3.8 articles_test.py 


## Technologies Used
* Python3.8
* Flask
* HTML
* CSS


## License
[MIT](https://github.com/KakushaVenecia/News/blob/master/LICENSE)

