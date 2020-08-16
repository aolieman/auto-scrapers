[![Animation of filled spreadsheet](https://keybase.pub/alioli/media/as24-sheet-demo.gif)](https://keybase.pub/alioli/media/as24-sheet-demo.mp4)

## Favorites Scraper for Autoscout24

### Setup Autoscout24 account
- Log in to https://autoscout24.nl using Google Chrome.
- Ensure that you have some offers in https://www.autoscout24.nl/account/favorites.

### Setup Web Scraper
- Install https://chrome.google.com/webstore/detail/web-scraper-free-web-scra/jnhgnonknehpejjnehehllkliplmbmhn?hl=en.
- See documentation at https://webscraper.io/documentation.
- Open Web Scraper: https://webscraper.io/documentation/open-web-scraper.
- "Create new sitemap" > Import Sitemap.
- Paste the contents of `autoscout24-favs.json`.
- "Import Sitemap" (button).

### Scrape car offers
- Open Chrome devtools (F12).
- Select Web Scraper tab.
- Select autoscout24-favs sitemap.
- Sitemap context menu > Scrape (⏳).
- Sitemap context menu > Export data as CSV.

You should now have a file named `autoscout24-favs.csv`.

### Load offer data into Google sheet
- Make a copy of https://docs.google.com/spreadsheets/d/1AvqqCzwGTLo-HxeRyzd7-rusWk0VaEeCBxlYDj1bTNA/edit?usp=sharing.
- Open the autoscout24-favs sheet.
- Select cell A1.
- File > Import: `autoscout24-favs.csv`.
- "Replace data at selected cell".
- Find & replace (Ctrl+H) "null" with an empty string.

See the formatted result in the "overview" sheet.
You may sort, filter, and set up views here.

## Add Route Data from Google Maps

### Setup Google Maps account
- Log in to Google Maps.
- Set your home address.
- Plan a route with your preferred mode of transport.

The scraper will use the home address that you set,
and will plan routes with the mode of transport that was last selected.

### Install Python v3.6+
See https://www.python.org/downloads/.
Windows 10 users can install Python from the Microsoft Store, 
or by typing `python` in a PowerShell window.

Please confirm your Python version by typing `python -v` into a shell.
You may have to use the `python3` program instead, if you also have an old v2.x installed.

### Scrape Google Maps data
- Run `python fill_maps_start_urls.py autoscout24-favs.csv google-maps.json` in a shell.
- In Web Scraper, go back to Sitemaps.
- Delete `google-maps` with the red button, if it exists.
- "Create new sitemap" > Import sitemap.
- Paste the updated `google-maps.out.json`.
- "Import Sitemap" (button).
- Sitemap context menu > Scrape (⏳).
- Sitemap context menu > Export data as CSV.

You should now have a file named `google-maps.csv`.

### Load travel data into Google sheet
- Open the google-maps sheet.
- Select cell A1.
- File > Import: `google-maps.csv`.
- "Replace data at selected cell".

The "overview" sheet should now include values in the route-distance 
and route-minutes columns.

## Legal Issues

Depending on your legal jurisdiction, limitations may apply to your use of this software.
Users are responsible for obtaining legal advice regarding their use of this software.

Usage of the Autoscout24 scraper may lead to a violation of the [EU Database Directive](https://en.wikipedia.org/wiki/Database_Directive)
or similar copyright protections. It could be argued that data exported from
the scraper is a partial reproduction of an Autoscout24 database. 
