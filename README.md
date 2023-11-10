# :oncoming_automobile::oncoming_police_car: Cardekho-Scraper & UsedCar-PricePrediction :oncoming_taxi::weight_lifting_man:
### **Developing a car price prediction model, combining data acquisition, preparation, analysis, modeling, and deployment**

Building a car price prediction model involves scraping data from reliable sources like CarDekho, cleaning and enhancing the dataset, exploring patterns, selecting a suitable machine learning algorithm, training and evaluating the model, tuning hyperparameters, deploying it into applications, and continuously monitoring and maintaining its performance for accuracy and reliability over time.

### About CarDekho :clown_face:

![cardekho](https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/62803edb-a79a-4afe-86c1-eb5063592e56)

CarDekho is a prominent online platform in the Indian automotive industry, offering a comprehensive range of services. Users can access detailed information, specifications, and reviews for various car models, aiding in informed decision-making. The platform features listings for both new and used cars, providing a marketplace for buying and selling vehicles. CarDekho also offers comparison tools, enabling users to assess different models based on specific criteria. Additionally, the website may provide automotive news and updates, covering new launches, reviews, and industry trends.

### :mechanical_leg: Steps Involved To Predict :mechanical_leg: 

1. Collect the Car links
2. Data Collection from Car links
3. Data Transformation into Structured data
4. Data Cleansing
5. Exploratory Data Analysis
6. Feature Engineering
7. Model Building
8. Evaluation and Validation
9. Deployment

### :man_shrugging: How we are going to predict the car price ? :woman_shrugging:

Collect the data of Car Details, Car Overview, Car Features, Car Specifications for each and every car. As we know that Kilo meter driven can be the important independent variable to predict the price. In the same way, year of manufacturing, features and specifications makes considerable impact in the car price. 

## :woman_technologist: 1. Collect the Car Links :man_artist:

### :supervillain_man: CarDekho Scraper

There are multiple filters available to see used cars based on Cities, Fuel Type, Brand. I am going to filter and collect data of the used cars by Cities. Click any of the cities.

<img width="789" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/20ca511a-2425-410c-a33c-a16f632009e4">

To intialize CarDekho Scraper below models has been utilized 

- selenium - For automating the pages
* BeautifulSoup - To get the html parser of the partcular page
+ pandas - To make the data into structured one

### :standing_person: Links Page :walking_man:

Since only 1580 links will be present in one page, So We will able to collect max 1500 links per cities. Code was written in such a way that it scrolls down end of the page and collects minimum of 1500 links when if the links are present more than 1500 in the particular page

<img width="849" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/4a9f696c-c8b8-44e1-aaf4-c508a5bc76e3">



I wrote a script to collect the links. You can find it in CarDekhoScrapperFile.ipynb file.

<img width="776" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/591ea3b3-5335-4906-8aec-4ffedd5dae96">

## :snowboarder: 2. Data Collection From Car Links :horse_racing:

After links are been scraped, now the time is to navigate all the cars page and collect the data. Multiple clicks has to be done on Features, Specifications to collect the data If we use selenium. It consumes a lot of time so here I have used combination of Selenium and BeautifulSoup to collect the data. 

Once we get into the car page we can send html.parser and collect the whole page html doc. From this we can extract all the data. Eventhough It takes almost 2hrs of time to complete 1200 links.

[Sample Car Link](https://www.cardekho.com/used-car-details/used-Kia-Sonet-Turbo-Dct-Anniversary-Edition-cars-Chennai_9a50ab47-7b87-4649-951d-fadcf4f77ceb.htm)

### :cartwheeling: 2.1 Car Details Data :wrestling:

<img width="881" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/abb9dfbf-0fd4-4ba0-8e10-816de2a986f5">

Collected Data

<img width="797" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/2c155e62-e546-43ca-ba7a-6e64555be5c4">


### :people_holding_hands: 2.2 Car Overview Data :right_anger_bubble:

<img width="545" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/d59c86d1-e816-4920-aeab-0f4941d24eb4">

Collected Data 

<img width="799" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/5e15d62d-06c6-4057-8781-d9064e6f0513">


### :raised_hand_with_fingers_splayed: 2.3 Car Features Data :metal:

<img width="455" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/e206ea74-0d33-426d-bdf1-af8ea1913c03">

Collected Data

<img width="799" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/24187c0b-1cb2-4c9f-adab-27639b22e054">


### :point_right: 2.4 Car Specs Data :point_left:

<img width="512" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/6f03ce36-38a6-4c47-9a44-84902b2ca734">

Collected Data

<img width="801" alt="image" src="https://github.com/karthickthangadurai/Cardekho-Scrapper-UsedCar-PricePrediction/assets/104092206/ef1c9b77-0f8d-4fb7-b083-640b3f1f5fcd">




