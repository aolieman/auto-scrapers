## Autoscout24 Favorites Scraper

### Setup Autoscout24
- log in to autoscout24.nl
- ensure that you have some offers in https://www.autoscout24.nl/account/favorites

### Setup Web Scraper
- Install https://chrome.google.com/webstore/detail/web-scraper-free-web-scra/jnhgnonknehpejjnehehllkliplmbmhn?hl=en
- see documentation at https://webscraper.io/documentation
- open Web Scraper: https://webscraper.io/documentation/open-web-scraper
- "Create new sitemap" > Import Sitemap
- paste the contents of autoscout24-favs.json
- "Import Sitemap" (button)

### Scrape car offers
- open devtools (F12)
- select Web Scraper tab
- select autoscout24-favs sitemap
- context menu > Scrape (⏳)
- context menu > Export data as CSV

### Load offer data into Google sheet
- Make a copy of https://docs.google.com/spreadsheets/d/1AvqqCzwGTLo-HxeRyzd7-rusWk0VaEeCBxlYDj1bTNA/edit?usp=sharing.
- open the autoscout24-favorieten sheet
- select cell A1
- File > Import: autoscout24-favs.csv
- "Replace data at selected cell"
- find & replace "null" with an empty string

## Add route data from Google Maps

### Setup Google Maps
- log in to Google Maps
- set your home address
- plan a route with your preferred mode of transport
- the scraper will use these settings

### Scrape Google Maps data
- copy `vendor-map` from autoscout24-favs.csv into maps-urls.txt
- deduplicate: `sort -uo maps-urls.txt maps-urls.txt` (linux)
- add the urls as a valid `startUrl` array into google-maps.json
- in Web Scraper, go back to Sitemaps
- delete `google-maps` with the red button
- Create new sitemap > Import sitemap
- paste the updated google-maps.json
- "Import Sitemap" (button)
- context menu > Scrape (⏳)
- context menu > Export data as CSV

### Load travel data into Google sheet
- open the google-maps sheet
- select cell A1
- File > Import: google-maps.csv
- "Replace data at selected cell"
