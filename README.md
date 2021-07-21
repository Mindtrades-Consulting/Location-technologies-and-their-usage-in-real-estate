# Location-technologies-and-their-usage-in-real-estate

# Introduction
In 2004, GPS technology combined with map viewing interfaces (TomTom GO being the forerunner for it) facilitated the arrival on navigation devices' market. (1)
Later in 2005, Google launched the web mapping product, Google Maps. And months later, the company sets in motion the Google Maps API that allows developers to embed Google Maps into an external website, onto which site-specific data can be overlaid.
This location technology has assisted millions, intrepid tourists, alley-hidden coffee shop owners, traffic gridlock commuters and even property haunters. The latter allows users to get very specific about their property requirements and quickly locate the exact properties they search for. This includes everything from ideal square footage, demographic data, proximity to areas of interest and so on.  
What’s interesting is that brokers and brokerages may already use the Google Maps API even without realizing it. So, why not take advantage of the data to know precisely how much impact specific points of interest (POI) can help increase property values or rental yield?
In this article, we establish a correlation between the price of several Seattle properties and the POI in their vicinity:

# Data Sources
The dataset was created by our team using Python packages requests (this request module allows you to send HTTP requests using Python), Selenium to scrape sources such as Zillow for real estate listings and Google Places API for Points of Interests close to these estates and positional information. 
The POIs we want to get are the ones not further than a mile away from the estate.
 You can find the data used in this article and much more in the github links below: 

# Data Analysis
We scrape accurate listings data from Zillow.
We use our google_api.py script to fetch the POIs not further than a mile away from each estate scraped in the previous point. And for this, we use Google Place API endpoint "nearbysearch' (https://maps.googleapis.com/maps/api/place/nearbysearch/).
We save the POIs in an array and attach them.
We use formatter.py's get_estate function to format our .json estates' data into a CSV; this code will also add three data columns representing the closest point of interest to that estate, its latitude, and its longitude coordinates.
We use formatter.py's get_POIS function to order POIs by their type.
We run data_processing.py to create maps and tables. 

# Hypothesis
1.    Combination of location technology and data analysis allows the user to locate relevant points of interest that can possibly impact the pricing of real estate. 
2.    Sometimes, there is a correlation between the price of a property and the points of interest in the vicinity.
 
# Summary: How can you benefit from this type of analysis
It is safe to say that the attributes of residential location, such as the proximity to place of employment, accessibility to health establishments and even neighborhood businesses, are among the major factors that determine not just the price of the house, but also the kind of potential buyer who is interested in them.

Realtors benefit greatly from this type of analysis. Most companies develop and curate huge datasets with tons of properties in the market; so, it’s easier to pinpoint a property a client may be interested in.
Location technology serves as a potential tool for developers, realtors, brokers  and clients to make informed, intelligent and confident decisions about their real estate investments. From POI nearby to demographic statistics, the variables to study and analyze are close to endless.
 
# How can MindTrades help?
MindTrades Consulting Services, a leading marketing agency provides in-depth analysis and insights for the global IT sector including leading data integration brands such as Diyotta. From Cloud Migration, Big Data, Digital Transformation, Agile Deliver, Cyber Security, to Analytics- Mind trades provides published breakthrough ideas, and prompt content delivery. For more information, check [mindtrades.com].

