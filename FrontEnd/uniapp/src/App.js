import {
  BrowserRouter as Router,
  Route,
  Routes,
  useLocation,
} from "react-router-dom";
import store from "./store";
import { Helmet, HelmetProvider } from "react-helmet-async";
import { Provider } from "react-redux";
import image from "assets/img/coding.png";

import AnimatedRoutes from "Routes";

function App() {
  return (
    <HelmetProvider>
      <Helmet>
        <title>Uniapp</title>
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
      <Provider store={store}>
        <Router>
          <AnimatedRoutes />
        </Router>
      </Provider>
    </HelmetProvider>
  );
}

export default App;
