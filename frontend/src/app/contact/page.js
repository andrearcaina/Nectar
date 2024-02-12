'use client';
import Image from 'next/image';
import Link from 'next/link';

export default function Contact() {
    return (
        <main className="container mx-auto p-8">
            <h1 className="text-2xl font-semibold text-yellow-400 mb-4">Contact Us! 🐝</h1>
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 my-[7rem]">
                <Link href="https://www.linkedin.com/in/andre-arcaina/" className="cursor-pointer bg-yellow-200 p-10 hover:shadow-md hover:scale-105 transition-transform rounded-lg">
                    <Image src="/images/andre.png" width={400} height={400} alt="Andre" className="mb-2 rounded-full mx-auhref w-40 h-40" />
                    
                    <h2 className="text-lg font-semibold mb-2">Andre</h2>
                    
                    <p className="text-gray-700 mb-2">2nd yr TMU CS student!</p>
                    <p className="text-gray-700">Fun fact: Wizard101 fan since 2009</p>
                    <br />
                    <p className="text-gray-700">Role: Fullstack Developer</p>
                </Link>
                
                <Link href="https://www.linkedin.com/in/sean-kwee-a87b2424b/" className="cursor-pointer bg-yellow-200 p-10 hover:shadow-md hover:scale-105 transition-transform rounded-lg">
                    <Image src="/images/sean.png" width={400} height={400} alt="Sean" className="mb-2 rounded-full mx-auhref w-40 h-40" />
                    
                    <h2 className="text-lg font-semibold mb-2">Sean</h2>
                    
                    <p className="text-gray-700 mb-2">2nd yr UofT CS student!</p>
                    <p className="text-gray-700">League gives me depression</p>
                    <br />
                    <p className="text-gray-700">Role: Backend Developer</p>
                </Link>
                
                <Link href="https://www.linkedin.com/in/tristan-cheng-147715256/" className="cursor-pointer bg-yellow-200 p-10 hover:shadow-md hover:scale-105 transition-transform rounded-lg">
                    <Image src="/images/tristan.png" width={400} height={400} alt="Tristan" className="mb-2 rounded-full mx-auhref w-40 h-40" />
                    
                    <h2 className="text-lg font-semibold mb-2">Tristan</h2>
                    
                    <p className="text-gray-700 mb-2">2nd yr TMU CS student!</p>
                    <p className="text-gray-700">t500 in OverWatch</p>
                    <br />
                    <p className="text-gray-700">Role: Frontend Developer</p>
                </Link>
                
                <Link href="https://www.linkedin.com/in/dominicchen1/" className="cursor-pointer bg-yellow-200 p-10 hover:shadow-md hover:scale-105 transition-transform rounded-lg">
                    <Image src="/images/dominic.png" width={400} height={400} alt="Dominic" className="mb-2 rounded-full mx-auto w-40 h-40" />
                    
                    <h2 className="text-lg font-semibold mb-2">Dominic</h2>
                    
                    <p className="text-gray-700 mb-2">2nd yr TMU CS student!</p>
                    <p className="text-gray-700">I love playing CoC and Clash Royale :D</p>
                    <br />
                    <p className="text-gray-700">Role: Frontend and UI/UX</p>
                </Link>
            </div>
        </main>
    );
}
