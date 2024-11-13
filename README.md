# remote-execution

This project is meant to act similar to how ssh would through firestore database

### Setup 

To set up the project, create a config folder and add the following three files there: <br>
- `host_config.py`
  - This file should include a variable `HOST_NAME = <your host name>`
- Firestore access key file
- `setup_firebase.py` which should be set up similar to the following:
```
import firebase_admin

cred = firebase_admin.credentials.Certificate('config/remote-execution-438cd-firebase-adminsdk-6uvno-0c8df829b2.json')
firestore_app = firebase_admin.initialize_app(cred)

print("successfully connected to the database!")
```

Now that you have added the required files, you can run the following to install the dependencies:
`pip install -r requirements.txt`

### Usage
To get started, you can run the `host.py` file on the device that you want gain remote access to
And to connect to the device, you can run the `client.py` file and choose the device you want to use from the menu


### How it works
The client script takes in the command you pass and adds it to the firestore database under the device that you are 
trying to access.<br>
Then on the host script it will look firestore events on the file objects being updated. Whenever there is a new command 
object available it will then run the command specified locally.<br> 
It will then add response objects to the database under the device with the response that came through the command line.
<br>The client will do a similar thing as the host and has events on the response collection updates. When a new response
is added to the database the client will read the message and print in the console.
<br><br>
And now we have a way remotely accessing the intended device!