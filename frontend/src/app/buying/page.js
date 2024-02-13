'use client';
import { useState } from 'react';
import { Form } from '@/components';

export default function selling() {
    const [data, setData] = useState('');

    const handleFormSubmit = (userInput) => {
        setData(userInput);
    }

    return (
        <main className="container mx-auto p-4 text-center min-height: 1000px">
            <h1 className="text-yellow-400 text-5xl font-bold p-8">Looking to buy something?</h1>
        
            <div className="mt-4">
                <p className="text-gray-600 text-2xl p-4 ">Enter your Amazon URL below to find related products and their prices!</p>
            </div>
        
            <Form onSubmit={handleFormSubmit} Prompt={"Enter URL!"} Name={"Buy"} Request={"buying"} />

            {(data && data.info) && (
                <div>
                    {data.info.map((item, index) => (
                        <div key={index} className="bg-white shadow-md rounded-lg p-4 mb-4">
                            <a className="text-blue-500 hover:underline" href={item.link} target="_blank">{item.title}</a>
                            <p className="text-gray-700">Price: ${item.price}</p>
                        </div>
                    ))}
                </div>
            )}
        </main>  
    );
}
