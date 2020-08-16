The purpose of this project was to scrap data from a website then create an HTML page to display that data. 

Data was scraped from the following urls:
https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
https://space-facts.com/mars/
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

In the scrape_mars.py file, a function was created to scrape and return saught data as a dictionary.

App.py was created to run the function, push the data to a mongos database, and run the index.html file using flask. 

Launching app.py with flask will bring you to the homepage. The homepage will be missing data until the user presses the "scrape" button. 
Doing this will update the homepage; the function to scrape and return the data will initiate. 

