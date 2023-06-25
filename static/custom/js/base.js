console.log("This is Base js file")
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



function handleButtonClick(param) {
    const csrfToken = getCookie('CSRF-TOKEN');
    var pk = param;  // Replace with the actual primary key value

    fetch(`/blog/like/${pk}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            'param1': param,
            'param2': 'value2'
        })
    })
    .then(response => {
        // Handle the response from the Django endpoint
        if (response.ok) {
            // Successful response
            return response.json();
        } else {
            // Handle error responses
            throw new Error('Error: ' + response.status);
        }
    })
    .then(data => {
        // Handle the data returned by the Django endpoint
        console.log(data);
    })
    .catch(error => {
        // Handle any errors that occurred during the request
        console.error(error);
    });
}