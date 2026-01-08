# Mastering-REST-APIs-with-FastAPI
Mastering REST APIs with FastAPI, by Packt Publishing

# What is a web API?

Just like the code file, but instead of one code file asking another file to do something one program asks another program over the internet.

1. This one by the client sending a request:
    1.1 GET /POST/HELLO where GET is a method and /POST/HELLO is an endpoint
2. A request is a few pieces of data, which are     inteperated by the server however it wishes ,by some standers
### RESTAPI

It is a set of architectural constraints.  When your API follows these constraints, then you can say it is a rest API.  

what are the rest constraints? 

the first thing is that in your system, you should use the concepts of client and server, most web API S do this. But what this means is you can't have a rest API between two Python files. 

The rest API should use the concept of a resource. 

Rest API S should be stateless. 

They should be cashable 

that you have a uniform hypermedia driven interface. 

### What is a resource?

Resources are just things that the API deals with just like classes in object oriented programming or rows in a database resources are what the API deals in. 

When a client makes a request, they should make a request about a particular resource. For example, if they want to get information about a post, they should say which post or if they want to get information about all posts, they should say that .

OK. So

### what does stateless mean?

 It just means the server doesn't keep any information about the individual clients. 

the server can't remember that the first request was about post three. That is what stateless means 

in every request, the client has to send all the relevant information for the server to understand what's going on. The server doesn't remember anything about the clients. 

### What does cachable mean?

If one client makes a request for information,  then it should be possible for the back end to save that response. So that when another client makes a request for the same information, it doesn't have to be recalculated.  Example, a client gets information for post with I D3, the API will go into the database and will fetch that information for the database and then we respond with it. If another client makes that request, maybe the server doesn't have to go to the database again because it's got that saved in a cache. 

This is not at odds with being stateless because the server isn't remembering which client asked for the information. It's simply streamlining the process of retrieving information that was recently used. So a cache is normally another layer in front of your API that remembers requests and the response that was sent back to that request. 


### What does multiple servers mean?

· Sometimes our backends are made up of multiple servers

· For example, one server for posts and comments

· Another for user authentication and registration

. The client shouldn't care about how the backend is organised!