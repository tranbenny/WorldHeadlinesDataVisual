World Map Data Visualization of Global News Reporting

App
  Client (Angular/ D3)
    - load data from custom api
    - load data onto custom data visualization
    - set up gulp/webpack build
    - create Angular structure for project
    - write tests for loading data


API (Flask, MySQL, Python)
  - create file to gather required information
      get NYTimes api call, DONE
      scrape news sites, get more news site's RSS feeds
        write a function that finds the country from an article title, DONE
            ISSUE: cannot find country if title/description only includes city names
      write a function to format times into date object

  - Figure out database schema
  - populate database with information
  - set up api routes with Flask to query information
      create status codes for responses
  - deploy a staging project online for testing api
