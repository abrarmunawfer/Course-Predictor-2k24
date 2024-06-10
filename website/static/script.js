document.getElementById('prediction-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const qualification = document.getElementById('qualification').value;
  const interest = document.getElementById('interest').value;
  const duration = document.getElementById('duration').value;

  // Perform your course prediction logic here
  // For this example, we'll just display a simple message

  const result = `Based on your qualification (${qualification}), interest (${interest}), and course duration (${duration}), we predict a course for you.`;

  document.getElementById('prediction-result').textContent = result;
});
