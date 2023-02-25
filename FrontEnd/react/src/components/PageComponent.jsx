export default function PageComponent({ title, buttons = "", children }) {
  return (
    <>
      <header className="bg-white shadow">
        <div className="py-6">
          <div className="flex justify-between items-center mx-auto max-w-7xl px-4 sm:px-6 md:px-8">
            <h1 className="text-2xl font-semibold text-gray-900">
              {title}
            </h1>
            {buttons}
          </div>
        </div>
        <div className="mx-auto max-w-7xl px-4 sm:px-6 md:px-8"></div>
      </header>
      <main className="flex-1">
        <div className="py-6">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 md:px-8">
            <h2 className="text-2xl font-semibold text-gray-900">
              {children}
            </h2>
          </div>
          <div className="mx-auto max-w-7xl px-4 sm:px-6 md:px-8"></div>
          {/* Replace with your content */}

          {/* /End replace */}
        </div>
      </main>
    </>
  );
}
