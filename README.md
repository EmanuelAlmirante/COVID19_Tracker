# COVID19 Tracker

This project served the purpose of learning the Django framework with a more hands-on approach while having a theme focused on the current situation the World is involved in. 


### Tech Stack:

- Python 3.8
- Django 3.0
- MySQL 5.7.29
- PyCharm

### Setup:

- Clone project to a folder
- Run the application with _python manage.py runserver 8080_

## Endpoints:

**Create record** - **POST** localhost:8080/api/covidtracker

URL:  
	
    localhost:8080/api/covidtracker
	
Body:
			
    {
        "country": "Portugal",
        "total_cases": 123,
        "new_cases": 1,
        "total_deaths": 12345,
        "new_deaths": 1,
        "total_recovered": 12345,
        "active_cases": 123,
        "day": "2018-03-29"
    }
		
Return:
		
    {
        "id": 3,
        "country": "Portugal",
        "total_cases": 123,
        "new_cases": 1,
        "total_deaths": 12345,
        "new_deaths": 1,
        "total_recovered": 12345,
        "active_cases": 123,
        "day": "2018-03-29"
    }
    
**Get all records** - **GET** localhost:8080/api/covidtracker

URL:  
	
    localhost:8080/api/covidtracker

Body:
			
    empty
		
Return:
		
    [
      {
          "id": 3,
          "country": "United Kingdom",
          "total_cases": 123,
          "new_cases": 1,
          "total_deaths": 12345,
          "new_deaths": 1,
          "total_recovered": 12345,
          "active_cases": 123,
          "day": "2018-03-29"
      }
    ]

**Update a record by id** - **PUT** localhost:8080/api/covidtracker/recordId/{recordId}

URL:  
	
    localhost:8080/api/covidtracker/recordId/1
    
Body:

    {
      "country": "United Kingdom",
      "total_cases": 123,
      "new_cases": 1,
      "total_deaths": 12345,
      "new_deaths": 1,
      "total_recovered": 12345,
      "active_cases": 123,
      "day": "2018-03-29"
    }
    
Return:

    {
        "id": 1,
        "country": "United Kingdom",
        "total_cases": 123,
        "new_cases": 1,
        "total_deaths": 12345,
        "new_deaths": 1,
        "total_recovered": 12345,
        "active_cases": 123,
        "day": "2018-03-29"
    }
    
**Get a record by id** - **GET** localhost:8080/api/covidtracker/recordId/{recordId}

URL:  
	
    localhost:8080/api/covidtracker/recordId/1

Body:

    empty
    
Return:

    {
        "id": 1,
        "country": "United Kingdom",
        "total_cases": 123,
        "new_cases": 1,
        "total_deaths": 12345,
        "new_deaths": 1,
        "total_recovered": 12345,
        "active_cases": 123,
        "day": "2018-03-29"
    }
    
**Delete a record by id** - **DELETE** localhost:8080/api/covidtracker/recordId/{recordId}

URL:  
	
    localhost:8080/api/covidtracker/recordId/1
    
Body:

    empty

Return:

    {
      "message": "Record was deleted successfully!"
    }
