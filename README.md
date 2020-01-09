# router

<img width="1408" alt="Screen Shot 2020-01-08 at 8 40 46 PM" src="https://user-images.githubusercontent.com/11286381/72038929-0627bd80-3258-11ea-92f5-510ff8915cab.png">

View a route on a map either using a controller or through URL parameters.

Paths:
- `/`: view a route with a controller
- `/route`: view a route with URL parameters.


### URL parameters

#### /route

- `origin`: Origin longitude and latitude, separated by a comma. i.e. `origin=<originLng,originLat>`
- `destination`: Destination longitude and latitude, separated by a comma. i.e. `destination=<destinationLng,destinationLat>`

e.g. /route?origin=-122.41926148222771,37.77929236933795&destination=122.27255309353512,37.80531006555853

<img width="756" alt="Screen Shot 2020-01-08 at 8 36 03 PM" src="https://user-images.githubusercontent.com/11286381/72038931-0758ea80-3258-11ea-9e27-5e53907b79e5.png">

### To run locally:

```sh
export MAPBOX_ACCESS_TOKEN='<...>' # Get your Mapbox access token from www.mapbox.com/account
sh start.sh
```
