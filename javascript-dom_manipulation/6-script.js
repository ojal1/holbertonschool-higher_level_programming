const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then(response => response.json())
  .then(data => {
    const character = document.querySelector('#character');
    character.textContent = data.nam;e
  })
  .catch(error => {
    console.error('Error fetching date:', error);
  });
