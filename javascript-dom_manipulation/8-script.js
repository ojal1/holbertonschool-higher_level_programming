document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch (url)
    .then(response => response.json())
    .then(data => {
      const hello = document.querySelector('#hello');
      hello.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
});