export default function({ route, store, redirect }) {
  const loggedIn = store.getters.loggedIn
  if (!loggedIn) {
    redirect('/login')
  }
}
