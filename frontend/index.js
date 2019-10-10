"use strict";


(async() => {
  const res = new Promise((resolve, reject) => {
    fetch('http://localhost:5000')
      .then(res => res.json())
      .then(res => resolve(res))
      .catch(err => reject(err))
  })
  document.body.innerHTML = await res
})();