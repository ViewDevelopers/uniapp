import { Fragment, useState } from "react";
import { Navigate, NavLink, Outlet } from "react-router-dom";
import { useStateContext } from "../contexts/ContextProvider";
import { Dialog, Transition, Disclosure, Menu } from "@headlessui/react";
import {
  Bars3Icon,
  ChartBarIcon,
  HomeIcon,
  UserIcon,
  UsersIcon,
  XMarkIcon,
  ArrowRightOnRectangleIcon,
  BuildingOffice2Icon,
  PencilSquareIcon,
  CalendarDaysIcon,
} from "@heroicons/react/24/outline";

const navigation = [
  { name: "Inicio", to: "/", icon: HomeIcon, current: true },
  { name: "Unidades", to: "/unidades", icon: BuildingOffice2Icon },
  { name: "Blog", to: "/blog", icon: PencilSquareIcon },
  {
    name: "Calendario",
    to: "/calendario",
    icon: CalendarDaysIcon,
  },
  { name: "Reportes", to: "/reportes", icon: ChartBarIcon },
  { name: "Usuarios", to: "/usuarios", icon: UsersIcon },
];

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

export default function DefaultLayout() {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const { currentUser, userToken } = useStateContext();

  // if (!userToken) {
  //   return <Navigate to="login" />;
  // }

  const logout = (ev) => {
    ev.preventDefault();
    console.log("Logout");
    // axiosClient.post("/logout").then((res) => {
    //   setCurrentUser({});
    //   setUserToken(null);
    // });
  };

  // useEffect(() => {
  //   axiosClient.get("/me").then(({ data }) => {
  //     setCurrentUser(data);
  //   });
  // }, []);

  return (
    <>
    {/* -------- Inicia Sidebar -------- // */}
      <div>
        <Transition.Root show={sidebarOpen} as={Fragment}>
          <Dialog
            as="div"
            className="relative z-40 md:hidden"
            onClose={setSidebarOpen}
          >
            <Transition.Child
              as={Fragment}
              enter="transition-opacity ease-linear duration-300"
              enterFrom="opacity-0"
              enterTo="opacity-100"
              leave="transition-opacity ease-linear duration-300"
              leaveFrom="opacity-100"
              leaveTo="opacity-0"
            >
              <div className="fixed inset-0 bg-gray-600 bg-opacity-75" />
            </Transition.Child>

            <div className="fixed inset-0 z-40 flex">
              <Transition.Child
                as={Fragment}
                enter="transition ease-in-out duration-300 transform"
                enterFrom="-translate-x-full"
                enterTo="translate-x-0"
                leave="transition ease-in-out duration-300 transform"
                leaveFrom="translate-x-0"
                leaveTo="-translate-x-full"
              >
                <Dialog.Panel className="relative flex w-full max-w-xs flex-1 flex-col bg-gray-900">
                  <Transition.Child
                    as={Fragment}
                    enter="ease-in-out duration-300"
                    enterFrom="opacity-0"
                    enterTo="opacity-100"
                    leave="ease-in-out duration-300"
                    leaveFrom="opacity-100"
                    leaveTo="opacity-0"
                  >
                    <div className="absolute top-0 right-0 -mr-12 pt-2">
                      <button
                        type="button"
                        className="ml-1 flex h-10 w-10 items-center justify-center rounded-full focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                        onClick={() => setSidebarOpen(false)}
                      >
                        <span className="sr-only">Close sidebar</span>
                        <XMarkIcon
                          className="h-6 w-6 text-white"
                          aria-hidden="true"
                        />
                      </button>
                    </div>
                  </Transition.Child>
                  <div className="h-0 flex-1 overflow-y-auto pt-5 pb-4">
                    <div className="flex flex-shrink-0 items-center px-4">
                      <img
                        className="h-12 w-auto"
                        src="./src/assets/img/imagotipo-uniapp.svg"
                        alt="Mgranada Asesores"
                      />
                      <h2 className="ml-2 text-lg font-medium text-neutral-50 group-hover:text-gray-900">
                        Uniapp
                      </h2>
                    </div>
                    <nav className="mt-5 space-y-1 px-2">
                      {navigation.map((item) => (
                        <NavLink
                          key={item.name}
                          to={item.to}
                          className={({ isActive }) =>
                            classNames(
                              isActive
                                ? "bg-gray-100 text-gray-900"
                                : "text-gray-600 hover:bg-gray-50 hover:text-gray-900",
                              "group flex items-center px-2 py-2 text-base font-medium rounded-md"
                            )
                          }
                        >
                          <item.icon
                            className={classNames(
                              item.current
                                ? "text-gray-500"
                                : "text-gray-400 group-hover:text-gray-500",
                              "mr-4 flex-shrink-0 h-6 w-6"
                            )}
                            aria-hidden="true"
                          />
                          {item.name}
                        </NavLink>
                      ))}
                    </nav>
                  </div>
                  <div className="flex flex-shrink-0 border-t border-gray-600 p-4">
                    <a href="#" className="group block flex-shrink-0">
                      <div className="flex items-center">
                        <div>
                          <UserIcon className="w-8 h-8 bg-black/25 p-2 rounded-full text-white" />
                        </div>
                        <div className="ml-3">
                          <div className="text-base font-medium text-neutral-50 group-hover:text-orange-200">
                            {currentUser.name}
                          </div>
                          <div className="text-base font-medium text-neutral-50 group-hover:text-orange-200">
                            {currentUser.email}
                          </div>
                          <p className="text-sm font-medium text-gray-500 group-hover:text-gray-700 py-1">
                            Ver perfil
                          </p>
                          <p className="text-xs font-medium text-gray-500 group-hover:text-gray-700 py-1">
                            Ajustes
                          </p>
                        </div>
                      </div>
                    </a>
                  </div>

                  {/* ------ Buttom Logout ------------ */}

                  <div className="flex items-center py-2">
                    <div className="flex flex-shrink-0 p-4">
                      <div className="flex items-center">
                        <div>
                          <button
                            type="button"
                            className="rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
                          >
                            <span className="sr-only">Logout</span>
                            <ArrowRightOnRectangleIcon
                              className="h-6 w-6"
                              aria-hidden="true"
                            />
                          </button>
                        </div>
                        <div className="ml-3">
                          <a
                            href="#"
                            onClick={(ev) => logout(ev)}
                            className={
                              "block px-1 py-2 text-sm text-neutral-50 font-semibold"
                            }
                          >
                            Cerrar Sesión
                          </a>
                        </div>
                      </div>
                    </div>
                  </div>
                </Dialog.Panel>
              </Transition.Child>
              <div className="w-14 flex-shrink-0">
                {/* Forzar el encogimiento de la barra lateral para que quepa el icono de cierre */}
              </div>
            </div>
          </Dialog>
        </Transition.Root>

        {/* ---------- Sidebar para Desktop -------------- */}

        <div className="hidden md:fixed md:inset-y-0 md:flex md:w-64 md:flex-col">
          {/* Sidebar component, swap this element with another sidebar if you like */}
          <div className="flex min-h-0 flex-1 flex-col border-r border-gray-900 bg-gray-900">
            <div className="flex flex-1 flex-col overflow-y-auto pt-5 pb-4">
              <div className="flex flex-shrink-0 items-center px-4">
                <img
                  className="h-14 w-auto"
                  src="./src/assets/img/imagotipo-uniapp.svg"
                  alt="Uniapp"
                />
                <h2 className="ml-2 text-lg font-medium text-neutral-50 group-hover:text-gray-900">
                  Uniapp
                </h2>
              </div>
              <nav className="mt-5 flex-1 space-y-1 bg-gray-900 px-2">
                {navigation.map((item) => (
                  <NavLink
                    key={item.name}
                    to={item.to}
                    className={({ isActive }) =>
                      classNames(
                        isActive
                          ? "bg-gray-100 text-gray-900"
                          : "text-gray-600 hover:bg-gray-50 hover:text-gray-900",
                        "group flex items-center px-2 py-2 text-sm font-medium rounded-md"
                      )
                    }
                  >
                    <item.icon
                      className={classNames(
                        item.current
                          ? "text-gray-500"
                          : "text-gray-400 group-hover:text-gray-500",
                        "mr-3 flex-shrink-0 h-6 w-6"
                      )}
                      aria-hidden="true"
                    />
                    {item.name}
                  </NavLink>
                ))}
              </nav>
            </div>
            <div className="flex flex-shrink-0 border-t border-gray-600 p-4">
              <a href="#" className="group block w-full flex-shrink-0">
                <div className="flex items-center">
                  <div>
                    <UserIcon className="w-8 h-8 bg-black/25 p-2 rounded-full text-white" />
                  </div>
                  <div className="ml-3">
                    <div className="text-sm font-medium text-neutral-50 group-hover:text-orange-200">
                      {currentUser.name}
                    </div>
                    <div className="text-sm font-medium text-neutral-50 group-hover:text-orange-200">
                      {currentUser.email}
                    </div>
                    <p className="text-xs font-medium text-gray-500 group-hover:text-gray-700 py-1">
                      Ver perfil
                    </p>
                    <p className="text-xs font-medium text-gray-500 group-hover:text-gray-700 py-1">
                      Ajustes
                    </p>
                  </div>
                </div>
              </a>
            </div>

            {/* ------ Buttom Logout ------------ */}

            <div className="flex items-center py-2">
              <div className="flex flex-shrink-0 p-4">
                <div className="flex items-center">
                  <div>
                    <button
                      type="button"
                      className="rounded-full bg-gray-800 p-1 hover:bg-red-500 focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
                    >
                      <a
                        href="#"
                        onClick={(ev) => logout(ev)}
                        className={"block px-3 py-3 text-sm text-neutral-50 font-semibold hover:text-white"}
                      >
                        Cerrar Sesión
                      </a>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="flex flex-1 flex-col md:pl-64">
          <div className="sticky top-0 z-10 bg-white pl-1 pt-1 sm:pl-3 sm:pt-3 md:hidden">
            <button
              type="button"
              className="-ml-0.5 -mt-0.5 inline-flex h-12 w-12 items-center justify-center rounded-md text-gray-500 hover:text-gray-900 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-gray-900"
              onClick={() => setSidebarOpen(true)}
            >
              <span className="sr-only">Open sidebar</span>
              <Bars3Icon className="h-6 w-6" aria-hidden="true" />
            </button>
          </div>
          <Outlet />
        </div>
      </div>
    </>
  );
}
