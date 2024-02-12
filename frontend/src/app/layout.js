import { Inter } from "next/font/google";
import { Navbar, Footer } from "@/components";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Nectar",
  description: "Comparison Web App!",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        <main className={inter.className}>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
