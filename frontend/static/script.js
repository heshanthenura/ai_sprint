function sendRequest() {
  const userInput = document.getElementById('userInput').value;
  const responseElement = document.getElementById('response');

  if (userInput.trim() === '') {
      responseElement.innerText = 'Please enter a valid query!';
      return;
  }

  // Send POST request to backend
  fetch('/query', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query: userInput })
  })
  .then(response => response.json())
  .then(data => {
      // Clear previous response
      responseElement.innerHTML = '';

      // Display results as a list
      if (data.length > 0) {
          const list = document.createElement('ul');
          data.forEach(item => {
              const listItem = document.createElement('li');
              listItem.textContent = item;
              list.appendChild(listItem);
          });
          responseElement.appendChild(list);
      } else {
          responseElement.innerText = 'No results found.';
      }

      // Clear input field
      document.getElementById('userInput').value = '';
  })
  .catch(error => {
      console.error('Error:', error);
      responseElement.innerText = 'An error occurred. Please try again.';
  });
}

// Enter key support
document.getElementById('userInput').addEventListener('keypress', function(event) {
  if (event.key === 'Enter') {
      sendRequest();
  }
});

