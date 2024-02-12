import Image from 'next/image';

export default function Carousel() {
    return (
        <div class="mt-[5rem] pictures">
            <div class="pictures-slide flex whitespace-nowrap"> 
                {Array(12).fill().map((_) => (
                    <div class="pictures-slide-item flex-shrink-0">
                        <Image
                            src={`/images/nectar.png`}
                            alt="carousel"
                            width={500}
                            height={500}
                            className='h-[100px] w-[100px] md:h-[300px] md:w-[300px] lg:h-[500px] lg:w-[500px] object-cover rounded-lg shadow-lg'
                        />
                    </div>
                ))}
            </div>
        </div>
    );
}
