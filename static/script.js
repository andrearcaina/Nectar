$(document).ready(function() {
    $('#user-input-form').click(function(e) {
        e.preventDefault();
        let user_input = $('#user-input').val();
        console.log(user_input);
        
        $.ajax({
            type: 'POST',
            url: '/process_input', 
            data: JSON.stringify({'user_input': user_input}),
            contentType: 'application/json',
    
            success: function(data) {
                $('#result').text(data.result);
            },
            
            error: function() {
                $('#result').text('Request failed.');
            }
        });
    });
});