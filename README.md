# Simple Middleware
A simple middleware that will register a service, lookup a service, handle multiple requests and facilitate the communication between the service consumer and the service provider.

[![N|Solid](https://user-images.githubusercontent.com/2020370/44630207-8e653580-a977-11e8-8b87-0252ea94c636.jpg)]()

## Start middleware
This will start the middleware and listen to client requests
```
cd Middleware
python main.py
```

## Start sample server
This will start a sample server (gcd service).
In the initialization it sends a request to register it on the service directory
```
cd Server
python gcd_service.py
```

## Start sample client
### Compile
```
cd Client
javac Client.java
```
### Run example
Example: To get GCD value of 12 & 18
```
java Client gcd 12 18
```

