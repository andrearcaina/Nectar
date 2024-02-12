'use client';

export default function About() {
    return (
        <main className="p-8">
            <h1 className="text-2xl font-semibold text-yellow-400 mb-4">About Nectar</h1>
            
            <p className="text-gray-700 mb-4">
                Nectar is on a mission to simplify your online shopping and selling experience. We strive to empower users by providing a reliable platform that offers comprehensive product comparisons, real-time pricing insights, and valuable decision-making tools. Our goal is to make online shopping and selling more transparent, convenient, and cost-effective for every user.
            </p>

            <br /><br />
            <hr className="border-gray-800" />
            <br /><br />
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                <div className="bg-white shadow-md rounded p-4">
                    <h2 className="text-xl font-semibold mb-2">Product Comparison</h2>
                    <p className="text-gray-700">Compare prices, ratings, and reviews from various e-commerce websites to find the best deals and high-quality products.</p>
                </div>
                
                <div className="bg-white shadow-md rounded p-4">
                    <h2 className="text-xl font-semibold mb-2">Real-time Pricing Insights</h2>
                    <p className="text-gray-700">Get real-time market pricing data in the "Buying" section, aiding informed purchasing decisions based on current market trends.</p>
                </div>
                
                <div className="bg-white shadow-md rounded p-4">
                    <h2 className="text-xl font-semibold mb-2">Product Recommendations</h2>
                    <p className="text-gray-700">Receive personalized product recommendations based on your preferences and search history, enhancing your shopping experience.</p>
                </div>
                
                <div className="bg-white shadow-md rounded p-4">
                    <h2 className="text-xl font-semibold mb-2">Average Market Price</h2>
                    <p className="text-gray-700">The "Selling" section displays the average market price of items, enabling you to set competitive prices when selling your products.</p>
                </div>
                
                <div className="bg-white shadow-md rounded p-4">
                    <h2 className="text-xl font-semibold mb-2">User-Friendly Interface</h2>
                    <p className="text-gray-700">Nectar features an intuitive and user-friendly interface designed for seamless navigation and a delightful user experience.</p>
                </div>
            </div>

            <br /><br />
            <hr className="border-gray-800" />
            <br /><br />
            
            <div className="text-gray-700 flex flex-col md:flex-row md:space-x-4">
                <div className="mb-4 md:w-1/3">
                    <p className="font-semibold mb-2">Innovation in Online Shopping</p>
                    <p>Nectar is born out of the desire to simplify the complexities of online shopping and selling. With a team of passionate experts, we've designed a one-stop solution that equips users with the information they need to make smart choices in the world of e-commerce.</p>
                </div>
                
                <div className="mb-4 md:w-1/3">
                    <p className="font-semibold mb-2">For Savvy Shoppers and Sellers</p>
                    <p>Whether you're a savvy shopper looking for the best deals or a seller aiming to maximize your profits, Nectar is here to support you. We believe that by providing transparency and convenience, we can revolutionize the way you interact with e-commerce platforms.</p>
                </div>
                
                <div className="md:w-1/3">
                    <p className="font-semibold mb-2">Your Trusted Partner</p>
                    <p>Nectar is more than just a comparison app; it's your trusted partner in making well-informed decisions. Join us on this journey and experience the future of online commerce with Nectar.</p>
                </div>
            </div>
            

            <br /><br />
            <hr className="border-gray-800" />
            <br /><br />
            
        </main>
    );
}
