# non starter kit instructions 
- https://github.com/sneas/react-nested-routes-example/blob/master/src/App.js was looking at nested routes, haven't figured out yet 

# updated instructos that should be moved into the starter kit 

- will use `VERCEL` later for deployment, not google hosting 

- make sure inside the right folder (./frontend)
- install the packages from the `package.json` list with `npm install` 
- check which firebase account: `firebase login` / move to proper account
- initiate a new firebase project using `firebase initi` 
- select these following options (typical): 
    - firestore 
    - functions
    - storage
- then give it a name 
- then go into FIREBASE and go to hosting, set thatup - this will then provide a CONFIG file, you can then copy those parameters into a .env file with this structure: 
```
  REACT_APP_FIREBASE_API_KEY= 
  REACT_APP_FIREBASE_AUTH_DOMAIN= 
  REACT_APP_FIREBASE_PROJECT_ID= 
  REACT_APP_FIREBASE_STORAGE_BUCKET= 
  REACT_APP_FIREBASE_MESSAGING_SENDER_ID= 
  REACT_APP_FIREBASE_APP_ID= 
  REACT_APP_FIREBASE_MEASUREMENT_ID= 
```
- then ENABLE ANALYTICS to get the `measurementId` permeter for the config file
- then go into firestore - and create a `Firestore Database`, not a real time (?) 
    - start in production mode 
    - can use this for rules:
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true;
    }
  }
}
```
- will then need to go into firestore, and make PRODUCITON mode is on so data is not deleted
- then go into `AUTHENTICATION` section and turn on EMAIL + GMAIL 
- then give it a quick spin - first make sure local works on: 
    - `npm start` 
    
    
- building for vercel: 
    - login to vercel, link up github account - select `create react app` as the default react type for framework 
    - everything else should work
    - when deploying to vercel, after associating it with a domain, will need to add that domain into firebase-auth as a authorized domain for the login to work
