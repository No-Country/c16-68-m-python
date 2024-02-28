import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import ToDo from "./components/ToDo";
import Calendario from "./components/Calendario";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="lista" element={<ToDo />}></Route>
        <Route path="calendario" element={<Calendario />}></Route>
      </Routes>
    </BrowserRouter>
    // <div className="App">
    //   <Todo />
    // </div>
  );
}

export default App;
