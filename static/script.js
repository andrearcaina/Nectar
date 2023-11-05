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
                $('#result1').text('Loading...🐝');
            },

            success: function(data) {
                const mean = Math.round(parseFloat(data.result[0]) * 10000) / 10000;
                const stde = Math.round(parseFloat(data.result[1]) * 10000) / 10000;
                const voli = data.result[2];

                $('#result1').text("Mean: $" + mean + " | Standard Deviation: " + stde + " | Volatility: " + voli);

                const infoText = "The mean is the average market price -- consider selling here. \n Volatility represents the degree of price variation -- if it is high your item either is very volatile, or your prompts are too broad. \n Standard Deviation is a measure of price volatility.";
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
    
                beforeSend: function() {
                    $('#result2').text('Loading...');
                },

                success: function(data) {
                    $('#result2').empty();
                    
                    $('#result2').empty();

                    // Iterate through the list of lists
                    for (let i = 0; i < data.result.length; i++) {
                        const sublist = data.result[i];
                        const price = sublist[0];
                        const title = sublist[1];
                        const link = sublist[2]; // Assuming the 3rd item is the link

                        // Create a card element using Tailwind CSS classes
                        const card = $('<div class="bg-white shadow-md rounded-lg p-4 mb-4">');

                        // Create a link element with Tailwind CSS classes
                        const linkElement = $('<a class="text-blue-500 hover:underline" href="' + link + '" target="_blank">').text(title);

                        // Create a price element using Tailwind CSS classes
                        const priceElement = $('<p class="text-gray-700">').text(`Price: $${price}`);

                        // Append the link and price to the card
                        card.append(linkElement, priceElement);

                        // Append the card to #result2
                        $('#result2').append(card);
                    }
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