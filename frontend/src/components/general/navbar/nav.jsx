import Link from 'next/link';
import Image from 'next/image';
import { useState, useEffect } from 'react';
import { NavMobile } from './nav-mobile';

export default function Nav() {
    const [NavItems, setNavItems] = useState([]);

    useEffect(() => {
        fetchNavItems();
    }, []);

    const fetchNavItems = async () => {
        try {
            const res = await fetch('/data/nav-items.json');
            const navItems = await res.json();
            setNavItems(navItems);
        } catch (error) {
            console.error("Error fetching nav-items data:", error);
        }
    };

    return (
        <nav className="shadow-xl p-4 sticky top-0 z-50 custom-font bg-yellow-400">
            <div className="flex items-center justify-between max-w-7xl mx-auto px-4">
                <div className="flex items-center">
                    <Link href="/">
                        <p className="flex items-center space-x-2 text-black">
                            <Image src="/images/icon.ico" alt="Logo" width={80} height={80} className="rounded-md logo-image w-[50px] h-[50px] md:w-[50px] md:h-[50px] lg:w-[80px] lg:h-[80px]" />
                            <span className="font-semibold text-3xl lg:text-5xl">Nectar</span>
                        </p>
                    </Link>
                </div>

                <div className="hidden lg:flex lg:items-center lg:w-auto">
                    <div className="flex flex-col lg:flex-row lg:space-x-4">
                        {NavItems.map((route, index) => (
                            <Link href={route.href} key={index}>
                                <p className="text-black font-bold text-3xl hover:scale-[1.15] transition-all duration-400">{route.text}</p>
                            </Link>
                        ))}
                    </div>
                </div>

                <NavMobile links={NavItems} />
            </div>
        </nav>
    );
};