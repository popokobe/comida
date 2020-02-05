import firebase from '~/plugins/firebase'

export const state = () => ({
  isLoggedIn: false,
  token: null
})

export const getters = {
  loggedIn(state) {
    return state.token !== null
  }
}

export const actions = {
  register(context, credentials) {
    firebase
      .auth()
      .createUserWithEmailAndPassword(credentials.email, credentials.password)
      .then(
        (res) => {
          this.$router.push('/login')
        },
        (err) => {
          alert(err.message)
        }
      )
  },
  login({ commit }, credentials) {
    firebase
      .auth()
      .signInWithEmailAndPassword(credentials.email, credentials.password)
      .then(
        (res) => {
          const token = firebase.auth().currentUser.email
          alert(`You are logged in as ${res.user.email}`)
          commit('login', token)
          this.$router.push('/home')
        },
        (err) => {
          alert(err.message)
        }
      )
  },
  logout({ commit }) {
    firebase
      .auth()
      .signOut()
      .then((res) => {
        commit('logout')
        this.$router.push('/login')
      })
  }
}

export const mutations = {
  login(state, token) {
    state.isLoggedIn = true
    state.token = token
  },
  logout(state) {
    state.isLoggedIn = false
    state.token = null
  }
}
