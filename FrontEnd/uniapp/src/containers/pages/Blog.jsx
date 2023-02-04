import Footer from "components/navigation/Footer";
import Navbar from "components/navigation/Navbar";
import Layout from "hocs/layouts/Layout";
import { useEffect } from "react";
import { Helmet } from "react-helmet-async";

function Blog() {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);
  return (
    <Layout>
      <Helmet>
        <title>Uniapp | Blog</title>
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
      <div className="pt-28">Blog</div>
      <Footer />
    </Layout>
  );
}
export default Blog;
