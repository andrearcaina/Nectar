import Link from 'next/link';

export default function Description() {
    return (
        <main class="flex flex-col items-center justify-center mt-44">
            <h1 class="text-lg sm:text-2xl md:text-3xl lg:text-5xl text-gray-800 font-bold text-center">A versatile solution for comparing</h1>
            <h1 class="text-lg sm:text-2xl md:text-3xl lg:text-5xl text-gray-800 font-bold text-center">product prices, conducting pricing</h1>
            <h1 class="text-lg sm:text-2xl md:text-3xl lg:text-5xl text-gray-800 font-bold text-center">research, and identifying similarities</h1>
            <h1 class="text-lg sm:text-2xl md:text-3xl lg:text-5xl text-gray-800 font-bold text-center">to enhance the shopping experience</h1>
            
            <div className="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4">
            <Link href="/about">
                <p className="bg-yellow-200 hover:bg-yellow-500 text-gray-700 font-bold py-4 px-6 rounded mt-10 mr-8 transition duration-300 ease-in-out transition-delay-100">
                    How does it Work?
                </p>
            </Link>

            <Link href="/buying">
                <p className="bg-yellow-500 hover:bg-yellow-700 text-gray-700 font-bold py-4 px-6 rounded mt-10 ml-8 transition duration-300 ease-in-out transition-delay-100">
                    Get Started
                </p>
            </Link>
            </div>
        </main>
    );
}
