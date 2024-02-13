import { useState } from 'react';

export default function Form({ onSubmit, Prompt, Name, Request }) {
    const [userInput, setUserInput] = useState('');

    const handleInputChange = (e) => {
        setUserInput(e.target.value);
    }

    const handleFormSubmit = async (e) => {
        e.preventDefault();
        
        try {
            const response = await fetch(`http://localhost:5000/api/${Request}?user_input=${userInput}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_input: userInput })
            });
            const data = await response.json();

            let mean, stde, voli, stats, infoText;

            if (Request === "selling") {
                mean = parseFloat(data.result[0]).toFixed(4);
                stde = parseFloat(data.result[1]).toFixed(4);
                voli = data.result[2];

                stats = `Mean: $${mean} | Standard Deviation: ${stde} | Volatility: ${voli}`;
                infoText = "The mean is the average market price -- consider selling here. \n Volatility represents the degree of price variation -- if it is high your item either is very volatile, or your prompts are too broad. \n Standard Deviation is a measure of price volatility.";
            } else if (Request === "buying") {
                const sublist = data.result[0];
                
                infoText = sublist.map(item => ({
                    link: item[3],
                    title: item[1],
                    price: item[0]
                }));
            }
            
            onSubmit({stats: stats, info: infoText});
        } catch (error) {
            console.error(error);
        }
    }

    return (
        <form onSubmit={handleFormSubmit} className="mt-4 p-8">
            <input 
                type="text" 
                placeholder={Prompt} 
                value={userInput} 
                onChange={handleInputChange} 
                required 
                className="p-4 w-full px-3 py-5 border rounded-lg" 
            />
            <button type="submit" className="mt-2 text-xl px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none">{Name}</button>
        </form>
    );
}
