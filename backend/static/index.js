document.getElementById("search-btn").addEventListener("click", () => {
  const searchInput = document.getElementById("search").value;

  if (!searchInput) {
    alert("Please enter some text.");
    return;
  }

  const formData = new FormData();
  formData.append("search", searchInput);

  fetch("/submit", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.text())
    .then((result) => {
      console.log(result);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
