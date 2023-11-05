$(document).ready(function() {
    $('#selling-input').click(function(e) {
        e.preventDefault();
        let user_input = $('#user-sell').val();
        console.log(user_input);
        
        if (user_input == '') {
            $('#result1').text('Please enter a valid prompt.');
            return;
        }

        $.ajax({
            type: 'POST',
            url: '/process_input', 
            data: JSON.stringify({
                'user_input': user_input,
                'additional_data': "selling"
            }),
            contentType: 'application/json',
    
            success: function(data) {
                $('#result1').text(data.result);
            },
            
            error: function() {
                $('#result1').text('Request failed.');
            }
        });
    });

    $('#buying-input').click(function(e) {
        e.preventDefault();
        let user_input = $('#user-buy').val();
        console.log(user_input);

        if(/^(http:\/\/www\.|https:\/\/www\.)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/.test(user_input)){
            console.log("valid");

            $.ajax({
                type: 'POST',
                url: '/process_input',
                data: JSON.stringify({
                    'user_input': user_input,
                    'additional_data': "buying"
                }),
                contentType: 'application/json',
    
                success: function(data) {
                    $('#result2').text(data.result);
                },
    
                error: function() {
                    $('#result2').text('Request failed.');
                }
            });
        } else {
            $('#result2').text("Invalid input. Please enter a valid URL.");
            return;
        }
    });
});