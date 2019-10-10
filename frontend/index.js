import 'babel-polyfill'

(async() => {
  const res = await new Promise((resolve, reject) => {
    fetch('http://localhost:5000')
      .then(res => res.json())
      .then(res => resolve(res))
      .catch(err => reject(err))
  })
  document.body.innerHTML = JSON.stringify(res)
})();

// WebSocket connection to 'ws://localhost:46263/' failed: Error in connection establishment: net::ERR_CONNECTION_REFUSED