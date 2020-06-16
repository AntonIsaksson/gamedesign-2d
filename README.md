# Milestone Project 4 - Game Design

### Project Info ### 
An app created with the Django Framework, where you can download, buy and order animated creations for your 2D-Games.

[![Build Status](https://travis-ci.org/AntonIsaksson/gamedesign-2d.svg?branch=master)](https://travis-ci.org/AntonIsaksson/gamedesign-2d)



### UX ###

The main UX goal with the website, is to provide a sence of fun and warmth. Colorful, but soft features, and a "round" font style will hopefullt accomplish this. At first glance you will get a quick overview of what the site has to offer.


#### User Stories: ####

1.	As a professional game-developer, I'm looking for objects to use in my 2D-games.  

2.	As a visitor that is making games as a hobby, I'm looking for objects to use in my 2D-games.

3.	As a designer, I'm looking for inspiration.                

#### Strategy ####

1. Target Groups:
-  Professional GameDevelopers
-  "Hobby" Developers
2. B2B/B2C:
-  The main focus of the website will be to focus on private customers (or smaller businesses).
3. Content/Focus:
-  I want to start off with maximum 3 focus areas and perhaps in time I will expand the site. A problem when looking at similar websites today is that their focus-area is to broad, wich could confuse the customer/visitor, in my opinion. 

#### Scope ####

A fun but clean layout and homepage, where just enough meets the eye at first glance. From there 

#### Structure ####

Firstly, I decided on the structure for the navigation and architecture of the website. I wanted it to be self-explanatory and easy to "move around", without having to use the "return-button". A sidebar was something that I decided on early to accomplish this. At this stage, I also decided on what type of paymentplan to use at this stage, and I thought that the best plan was a Subscription Based plan, where you as a customer pay a small amount of money everymonth the get access to more and better content.  

#### Surface & Skeleton ####

![Wireframe](/wireframe/MileStoneProject4-WireFrame.pdf)

(if can't load wirefram PDF, please see folder /wireframe)


### Features ###

#### Existing Features ####

-   Register: lets a visitor register with a unique username and password. 
-	Log In: lets a user log in.
-	Log Out: lets an already logged in user log out.
-	Stripe: for Membership subscription
-	Order Item: a form where you can inquire for a unique, specially customized design. 
-   Search: a search-function where you search for items based on their names.



#### Features Left to Implement ####

In the future:
- Filling up the database with a bunch of designs of my own creation.
- I would like to make it possible for users to comment and rate on the items. 

### Technologies Used ###

-   Python (Django)
-   Postgres (as Database)
-	HTML
-	CSS
-   Javascript (jQuery)
-	Bootstrap 4.1.0: https://getbootstrap.com/
-	Pixabay: https://pixabay.com/
-   AWS: for media and static storage
-   Stripe: for payment



##### Testing Responsiveness #####
The code and website have been tested through-out a number of different Browsers (Chrome, Firefox, Explorer) and on a number of different devices via Google Chromes Developer Tools, to check responsiveness (different mobile devices like Iphone & Samsung Galaxy, Ipad, etc.) 


### Errors/Problems ### 

1. Downloading the files: due to (I think) some kind of security setting with/in AWS, I'm not able to download the files with the download attribute. For now, users can open the image in a seperate tab and save the image. 

### Deployment ###

The website is deployed on Heroku. To check out the live website, follow this link: https://gamedesign-2d.herokuapp.com/
Github: https://github.com/AntonIsaksson/gamedesign-2d 

### Content ###

All written content is made by myself.

### Media ###

Most pictures are taken from https://pixabay.com/ and stored in a AWS S3 Bucket. 


## Inspirations/Acknoweledgements

Fonts: https://artisanthemes.io/best-google-fonts-color-combinations-feminine-website/

Tutorial: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

Tutorial for Subscription: https://www.youtube.com/watch?v=zu2PBUHMEew