function sendRequest() {
  const userInput = document.getElementById('userInput').value;
  const responseElement = document.getElementById('response');

  responseElement.innerHTML = '<div class="loader"></div>';



  if (userInput.trim() === '') {
      responseElement.innerText = 'Please enter a valid query!';
      return;
  }

  $.ajax({
    url: '/submit',
    type: 'POST',
    data: { 'search': userInput },
    success: function(response) {
        console.log(response);
        
        responseElement.innerHTML = '';


        for (let i = 0; i<response.length; i++){
            let x = response[i];

            let keys = Object.keys(x);
            var price = JSON.stringify(x[keys[2]], null, 2);
            const cardHTML = `
                <div class="card" onclick="window.open('${x[keys[1]]}','_blank');">
                    <img src="${x[keys[0]]}" alt="${x[keys[3]]}">
                    <div class="text-elements">
                            <h2>${x[keys[3]]}</h2>
                            <p>Price: ${price}</p>
                    </div>
                </div>
            `;
            
            responseElement.innerHTML += cardHTML;
        }

    },
    error: function(error) {
        console.log(error);
    }
});



//   const formData = new FormData();
//   formData.append("search", userInput);



//   // Send POST request to backend
//   fetch('/submit', {
//       method: 'POST',
//       body: formData,
//   })
//   .then(response => response.json())
//   .then(jsonData => {
//     const cardContainer = document.getElementById('card-container');
//     const cardHTML = `
//         <div class="card">
//             <img src="${jsonData.imageURL}" alt="${jsonData.title}">
//             <h2>${jsonData.title}</h2>
//             <p>Price: Rs. ${jsonData.price.min} - Rs. ${jsonData.price.max}</p>
//         </div>
//     `;
//     cardContainer.innerHTML = cardHTML;
//   })
//   .catch(error => {
//       console.error('Error:', error);
//       responseElement.innerText = 'An error occurred. Please try again.';
//   });
}

function hasSubJson(obj, key) {
    return typeof obj[key] === "object" && obj[key] !== null && !Array.isArray(obj[key]);
}