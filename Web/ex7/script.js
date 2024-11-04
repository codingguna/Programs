const form = document.getElementById('user-form');
const userlist = document.getElementById('user-list');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const phone = document.getElementById('phone').value;
  const user = { name, email, phone };
  const listItem = document.createElement('tr');
  listItem.innerHTML = `<td>${user.name}</td><td>${user.email}</td><td>${user.phone}</td><td><button class="delete">Delete</button>`;
  userlist.appendChild(listItem);

  const deleteBtn = listItem.querySelector('.delete');
  deleteBtn.addEventListener('click', (e) => {
    const row = deleteBtn.parentNode.parentNode;
    row.remove();
  });

  document.getElementById('name').value = '';
  document.getElementById('email').value = '';
  document.getElementById('phone').value = '';
});