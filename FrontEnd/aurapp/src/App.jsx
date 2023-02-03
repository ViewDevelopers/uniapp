import { useState } from "react";

function App() {
  const [count, setCount] = useState(0);

  return (
    <section>
      <div>
        <div className="text-blue-700 text-5xl text-center font-bold underline">
          <h1>Bienvenidos a Aurapp</h1>
        </div>
      </div>
    </section>
  );
}

export default App;
