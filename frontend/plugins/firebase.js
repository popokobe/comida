import firebase from 'firebase'

if (!firebase.apps.length) {
  firebase.initializeApp({
    apiKey: 'AIzaSyDPOy8YeWJNYNFpZ1Scralyu3ogXgAG8z4',
    authDomain: 'comida-deaa0.firebaseapp.com',
    databaseURL: 'https://comida-deaa0.firebaseio.com',
    projectId: 'comida-deaa0',
    storageBucket: 'comida-deaa0.appspot.com',
    messagingSenderId: '247515350718'
  })
}

export default firebase
