# Flask-RESTful-API

PYTHON VERSION - 2.7.18
Link-to: https://www.python.org/downloads/release/python-2718/


TECH STACK: Python, Flask, Flask-RESTful, Flask-JWT, SQLite3


This Flask application is a small project that I programmed to learn the basics of Web Dev with Flask & Python.

Overall Description:

  This Flask app is designed to demonstrate my knowledge of the framework. Simulating a store, the client can fetch, create, update, and delete items in the SQLite3 relational database. However, in order to access this API, the client must register and have a JWT authorization token in their header. Set-up instructions are included below this section.  

  Features Include:
    Registering a user to a sqlite3 database
    Authenticating the user and returning a JWT access token
    A lock on the Item API that requires an Authorization header with the users JWT access token
    Fetch all items in database
    Fetch a single item in database
    Create a single item in database
    Update price of a single existing item in database / create it if non-existing
    Delete a single item in database

  The following routes are supported:
    POST /register
    POST /auth
    GET /items
    GET /item/<name_of_item> (EX: /item/sofa)
    POST /item/<name_of_item>
    PUT /item/<name_of_item>
    DELETE /item/<name_of_item>
    
__________________________________________________________
  
Set-up Instructions:
 Clone into this repository:
   git clone https://github.com/blakeroy01/Flask-RESTful-API.git:
      
 Install neccessary packages:
   Flask:
     pip install Flask
        
   Flask-RESTful:
     pip install Flask-RESTful
        
   Flask JWT:
     pip install Flask-JWT

  CREATE SQL TABLES (items and users)
  Ensure you are inside the correct directory, and run:
    python create_tables.py
    
   You should see a data.db file has been instantiated.
   
   At this point, you may decide to run the app:
    python app.py
    
   You should recieve the following message:
     * Serving Flask app "app" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 320-029-098
     
   Now you can test the endpoints.
   
__________________________________________________________

Testing Instructions:
  IMPORTANT NOTE: Ensure the body of all requests are in JSON format
  
  1.) Register User | Method Type : POST 
    http://127.0.0.1:5000/register
    
    Format:
      {
        "username": "your_username",
        "password": "your_password"
      }
      
      BOTH FIELDS ARE REQUIRED, HOWEVER, ERROR HANDLING WITH ERROR MESSAGE WILL OCCUR WITHOUT ONE OR BOTH.
      
          DESIRED OUTPUT:
          {
              "message": "User Created Successfully"
          }

          EXISTING USER:
          {
              "message": "User with that username already exists"
          }

          BAD REQUEST:
          {
            "message": {
                "password": "Password can not be left blank"
            }
          }

          {
            "message": {
                "username": "Username can not be left blank"
            }
          }
          
  2.)Authenticate User | Method Type : POST       
      http://127.0.0.1:5000/auth
      
      Format:
        {
          "username": "your_username",
          "password": "your_password"
        }
        
        BOTH FIELDS ARE REQUIRED, HOWEVER, ERROR HANDLING WITH ERROR MESSAGE WILL OCCUR WITHOUT ONE OR BOTH.
            DESIRED OUTPUT:
            {
              "access_token":         "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MywiaWF0IjoxNjEwMzgyMTQ5LCJuYmYiOjE2MTAzODIxNDksImV4cCI6MTYxMDM4MjQ0OX0.QSTSp9uuEaJpcKShHVbasynmGBMI6g9dfCRJH1Svoag"
            }
            
            BAD REQUEST
            {
            "description": "Invalid credentials",
            "error": "Bad Request",
            "status_code": 401
            }
            
            COPY AND PASTE THIS ACCESS TOKEN INTO YOUR HEADER LIKE SO:
            KEY: AUTHORIZATION | VALUE: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MywiaWF0IjoxNjEwMzgyMTQ5LCJuYmYiOjE2MTAzODIxNDksImV4cCI6MTYxMDM4MjQ0OX0.QSTSp9uuEaJpcKShHVbasynmGBMI6g9dfCRJH1Svoag
            
            IT IS VERY IMPORTANT TO ADD JWT AND A SPACE BEFORE PASTING THE ACCESS TOKEN INTO YOUR VALUE SLOT.
            
  3.)The API Endpoints | METHODS : GET, POST, PUT, DELETE
      With your valid JWT authorization token in the header, you may now access the API. KEEP IN MIND: it may expire during your session in that case, you will have to get a new one from the `/auth` endpoint
      
      
      START WITH:
        POST
        http://127.0.0.1:5000/item/item_name
        
        Format:
          {
              "price": 15.99
          }
          
         This will create the item
         
         GET
         http://127.0.0.1:5000/item/item_name
         
         This will return the item
         
         PUT
         http://127.0.0.1:5000/item/item_name
         
         Format:
          {
              "price": 18.99
          }
          
         This will update the price of the item / create it if it does not exist
         
         DELETE
         http://127.0.0.1:5000/item/item_name
         
         This will remove the item from the SQLite database.
         
         /items endpoint COMING SOON TO RETRIEVE ALL ITEMS
         
        
  
