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
            
            beforeSend: function() {
                $('#result1').text('Loading...');
            },

            success: function(data) {
                const mean = Math.round(parseFloat(data.result[0]) * 10000) / 10000;
                const stde = Math.round(parseFloat(data.result[1]) * 10000) / 10000;
                const voli = data.result[2];

                $('#result1').text("Mean: $" + mean + ", Standard Deviation: " + stde + ", Volatility: " + voli);

                const infoText = "You should consider selling at this price. Volatility represents the degree of price variation, and Standard Deviation is a measure of price volatility.";
                $('#additional-info').text(infoText);
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