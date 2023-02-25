import { Outlet } from 'react-router-dom';


export default function GuestLayout() {
  return (
    <>
      <div>
        <div className="flex min-h-full items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
          <div className="w-full max-w-md space-y-8">
            <div>
              <a href="/">
                <img
                  className="mx-auto h-20 w-auto"
                  src="./src/assets/img/imagotipo-uniapp.svg"
                  alt="Mgranada Asesores"
                />
              </a>
            </div>
            <Outlet />
          </div>
        </div>
      </div>
    
    </>
  );
}



