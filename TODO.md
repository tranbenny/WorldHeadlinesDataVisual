World Map Data Visualization of Global News Reporting

App
  Client (Angular/ D3)
    - load data from custom api
    - load data onto custom data visualization
    - set up gulp build, DONE
      - include browerSync, babel for ES6, browserify, DONE 
    - create Angular structure for project
    - write tests for loading data
  Server:
    - wire up node backend to serve main page


API (Flask, MySQL, Python)
  - create file to gather required information, DONE
      get NYTimes api call, DONE
      scrape news sites, get more news site's RSS feeds, DONE
        write a function that finds the country from an article title, DONE
      write a function to format times into date object, DONE

  - Figure out database schema, DONE
  - populate database with information, DONE
  - set up api routes with Flask to query information
      create read statements for api's
      create status codes for responses
  - deploy a staging project online for testing api
  - write tests for reading from database
