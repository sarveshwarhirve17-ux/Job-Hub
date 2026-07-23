from fastapi import FastAPI
from fastapi import Form
import psycopg2                                    #psycopg2 lets python talk to postgresql
from fastapi.middleware.cors import CORSMiddleware

conn = psycopg2.connect(
    database="jobhub",
    user="postgres",

    password ="saru",
    host ="localhost",
    port="5432"
)

conn1 = psycopg2.connect(
    database="posts",
    user="postgres",

    password ="saru",
    host ="localhost",
    port="5432"
)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

@app.get("/")
def home():
    return{"message": "Job Hub Bankend Running"}



@app.post("/signup")
def signup(name:str = Form(),email:str=Form(),password:str=Form()):     # name:str = Form() == this is for name ,email:str=Form() == this is for email,password:str=Form() == this is for password
    cursor = conn.cursor()
    cursor.execute("INSERT INTO job(name,email,password) VALUES(%s,%s,%s)",(name,email,password))
    conn.commit()
    return{
        "name":name,                                                     # there will we enter the name 
        "email": email,                                                   # there will we enter the email
        "password": password,                                             # there will we enter the password
        "message":"Signup Successfull"
    }


@app.post("/login")
def login(email:str = Form(),password:str = Form()):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM job WHERE email = %s AND password =%s", (email,password))
    user = cursor.fetchone()

    if user:
        return{"Login Succesfull"}

    else:
        return{"invalid email or password"}    


@app.get("/profile")
def profile():
    return{"message": "profile shown Successfull"}



@app.post("/post")
def post(post:str = Form()):
    cursor = conn1.cursor()
    cursor.execute("INSERT INTO text(post) VALUES(%s)",(post,))
    conn1.commit()
    return{"message": "posts shown Successfull"}



@app.get("/posts")
def post():
    cursor = conn1.cursor()
    cursor.execute("SELECT * FROM text")
    posts = cursor.fetchall()
    
    return posts

