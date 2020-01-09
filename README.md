# router

<insert screen shot>

View a route on a map either using a controller or through URL parameters.

Paths:
- `/`: view a route with a controller
- `/route`: view a route with URL parameters.


### URL parameters

#### /route

- `origin`: Origin longitude and latitude, separated by a comma. i.e. `origin=<originLng,originLat>`
- `destination`: Destination longitude and latitude, separated by a comma. i.e. `destination=<destinationLng,destinationLat>`

e.g. /route?origin=-122.41926148222771,37.77929236933795&destination=122.27255309353512,37.80531006555853

<insert screenshot>

### To run locally:

```sh
export MAPBOX_ACCESS_TOKEN='<...>' # Get your Mapbox access token from www.mapbox.com/account
sh start.sh
```
