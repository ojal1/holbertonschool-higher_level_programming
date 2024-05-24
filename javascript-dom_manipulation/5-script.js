const upddateHeader = document.querySelector('#update_header');

upddateHeader.addEventListener('click', function() {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
});
