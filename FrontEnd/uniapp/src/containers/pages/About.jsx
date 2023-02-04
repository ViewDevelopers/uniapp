import Clients from "components/about/Clients";
import Features from "components/about/Features";
import Header from "components/about/Header";
import Images from "components/about/Images";
import Team from "components/about/Team";
import TestStats from "components/about/TestStats";
import Footer from "components/navigation/Footer";
import Navbar from "components/navigation/Navbar";
import Layout from "hocs/layouts/Layout";
import { useEffect } from "react";
import { Helmet } from "react-helmet-async";

function About() {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);
  return (
    <Layout>
      <Helmet>
        <title>Uniapp | Nosotros</title>
        <meta name="description" content="Uniapp | Managements Services" />
        <meta
          name="keywords"
          content="Aplicacion de administración y gestión administrativa"
        />
        <meta name="robots" content="all" />
        <link rel="canonical" href="https://www.uniapp.com/" />
        <meta name="author" content="Uniapp" />
        <meta name="publisher" content="Uniapp" />

        {/* Social Media Tags */}
        <meta property="og:title" content="Uniapp | Managements Services" />
        <meta
          property="og:description"
          content="Aplicación de administración y gestión de unidades residenciales. Servicios de administración y gestión de unidades residenciales."
        />
        <meta property="og:url" content="https://www.uniapp.com/" />
        <meta property="og:image" content="image" />

        <meta name="twitter:title" content="Uniapp | Managements Services" />
        <meta
          name="twitter:description"
          content="Aplicación de administración y gestión de unidades residenciales. Servicios de administración y gestión de unidades residenciales."
        />
        <meta name="twitter:image" content="image" />
        <meta name="twitter:card" content="summary_large_image" />
      </Helmet>

      <Navbar />
      <div className="pt-28">
        <Header />
        <TestStats />
        <Images />
        <Clients />
        <div className="bg-white">
          <div className="mx-auto max-w-7xl py-12 px-4 sm:px-6 lg:px-8">
            <div className="grid grid-cols-2 gap-8 md:grid-cols-6 lg:grid-cols-5">
              <div className="col-span-1 flex justify-center md:col-span-2 lg:col-span-1">
                <img
                  className="h-12"
                  src="https://tailwindui.com/img/logos/tuple-logo-gray-400.svg"
                  alt="Tuple"
                />
              </div>
              <div className="col-span-1 flex justify-center md:col-span-2 lg:col-span-1">
                <img
                  className="h-12"
                  src="https://tailwindui.com/img/logos/mirage-logo-gray-400.svg"
                  alt="Mirage"
                />
              </div>
              <div className="col-span-1 flex justify-center md:col-span-2 lg:col-span-1">
                <img
                  className="h-12"
                  src="https://tailwindui.com/img/logos/statickit-logo-gray-400.svg"
                  alt="StaticKit"
                />
              </div>
              <div className="col-span-1 flex justify-center md:col-span-3 lg:col-span-1">
                <img
                  className="h-12"
                  src="https://tailwindui.com/img/logos/transistor-logo-gray-400.svg"
                  alt="Transistor"
                />
              </div>
              <div className="col-span-2 flex justify-center md:col-span-3 lg:col-span-1">
                <img
                  className="h-12"
                  src="https://tailwindui.com/img/logos/workcation-logo-gray-400.svg"
                  alt="Workcation"
                />
              </div>
            </div>
          </div>
        </div>
        <Features />
        <Team />
        <div className="bg-white">
          <div className="mx-12 max-w-full py-12 px-4 sm:px-6 lg:flex lg:items-center lg:justify-between lg:py-16 lg:px-8">
            <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              <span className="block">Prueba la aplicación sin compromisos</span>
              <span className="block text-indigo-600">
                Solicita un demo gratis
              </span>
            </h2>
            <div className="mt-8 flex lg:mt-0 lg:flex-shrink-0">
              <div className="inline-flex rounded-md shadow">
                <a
                  href="#"
                  className="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-5 py-3 text-base font-medium text-white hover:bg-indigo-700"
                >
                  Empecemos
                </a>
              </div>
              <div className="ml-3 inline-flex rounded-md shadow">
                <a
                  href="#"
                  className="inline-flex items-center justify-center rounded-md border border-transparent bg-white px-5 py-3 text-base font-medium text-indigo-600 hover:bg-indigo-50"
                >
                  Más información
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </Layout>
  );
}
export default About;
