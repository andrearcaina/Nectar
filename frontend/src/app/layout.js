import { Navbar, Footer } from "@/components";
import "./globals.css";

export const metadata = {
  title: "Nectar",
  description: "Comparison Web App!",
  icons: [{ url: '/images/icon.ico', rel: 'icon' }]
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="bg-gray-100">
        <Navbar />
        <main className="space-y-20 min-h-[80vh]">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
