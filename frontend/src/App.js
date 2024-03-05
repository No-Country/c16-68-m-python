import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom'; 
import RegisterForm from './components/Register/RegisterForm';
import LoginForm from './components/Login/LoginForm';
import RastreoEmociones from './pages/RastreoEmociones';

function App() {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<h1>Bienvenido</h1>} />
        <Route path='register' element={<RegisterForm/>} />
        <Route path='login' element={<LoginForm/>} />
      </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
