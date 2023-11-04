document.getElementById('user-input-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const user_input = document.getElementById('user-input').value;
    fetch('/process_input', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_input }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
