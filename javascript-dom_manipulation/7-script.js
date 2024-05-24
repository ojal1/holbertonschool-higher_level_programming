const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch (url)
  .then(response => response.json())
  .then(data => {
    const listMovies = document.querySelector('#list_movies');
    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      listMovies.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
