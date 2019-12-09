# Restaurant Randomizer
 
Usage:
 To use Restaurant Randomizer follow these steps:
  1) Download Python 3.6.4
  2) Install Django using "pip install -U django"
  3) Install Google Maps using "pip install -U googlemaps"
  4) Clone the Restaurant Randomzier Frontend repository and follow the installation instructions found here: https://github.com/stanleyyoang/restaurant-randomizer-frontend
  5) Clone this repository to your desired location
  6) Navigate to the ~/RestaurantRandomizer/restuarantrandomizer folder in the command line
  7) In the command line type in "python manage.py runserver" and the server will be available for use by the frontend phone emulator

As of now, Restaurant Randomizer does not work in the emulator but will work in the browser
Start the server and enter http://localhost:8000/findfood/?cuisine=American,+Italian&minPrice=1&maxPrice=4&radius=20+miles&lon=-101.914&lat=33.608&minRating=1&maxRating=4 into the url and the chosen restaurant will appear on the server command line.
