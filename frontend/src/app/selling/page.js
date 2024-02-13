'use client';
import { useState } from 'react';
import { Form } from '@/components';

export default function selling() {
    const [data, setData] = useState(true);

    const handleFormSubmit = (userInput) => {
        setData(userInput);
    }

    return (
        <main className="container mx-auto p-4 text-center min-height: 1000px">
            <h1 className="text-yellow-400 text-5xl font-bold p-8">Selling</h1>
        
            <div className="mt-4">
                <p className="text-gray-600 text-2xl p-4 ">Prompt the form like: "shoe black nike" with spaces in between.</p>
            </div>
        
            <Form onSubmit={handleFormSubmit} Prompt={"Enter your item description"} Name={"Sell"} Request={"selling"} />

            {data !== null && data !== "" ? (
                <div>
                    <div class="mt-4 text-xl text-red-600">{data.stats}</div>
                    <div class="pt-10 pb-10 mt-4 text-l text-gray-700">{data.info}</div>
                </div>
            ) : 
                <div class="mt-4 text-xl text-red-600">Request failed.</div>
            }
        </main>  
    );
}
