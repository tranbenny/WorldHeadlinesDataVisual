APPLICATION TODO: 
- create a docker compose file for managing services 
- organize test files into test suites 


DatabaseAccess TODO:
- add timeout errors for mongodb connection

HeadlineData TODO: 
- add more tests for headline scraping
- create a program that checks if the country locating is correct 


HeadlineDataSummaryAPI TODO:
- create a check that requests have date parameters 
- add authorization for api routes 


Client TODO:
- create route that serves html, js, css files for frontend app

Database Cleaning TODO:
- make sure country_names is only one word, other names need to be added to 'other_names', DONE 
- remove the urlencoded characters from title and description in headlines 
- clean up regions data 
- add three letter country code to db 
- add geographical regions/cities to list of terms 
- presidents/government officials
- companies 

- make a special case for "North/South Korea" and other country names with spaces 
    - do a check for all countries that are more than one word 
    - use n-grams
    - Taiwan didn't match with anything
    - check U.S, U.S.
    - Soviet Union



