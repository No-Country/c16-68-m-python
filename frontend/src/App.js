
import { Toaster } from 'react-hot-toast';
import './App.css'; 
import RegisterForm from './components/Register/RegisterForm';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import LoginForm from './components/Login/LoginForm';

function App() {

  return ( 
    <>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<h1>Bienvenido</h1>} />
        <Route path='register' element={<RegisterForm/>} />
        <Route path='login' element={<LoginForm/>} />
      </Routes>
      <Toaster position='top-center'/>
    </BrowserRouter>
    </>
  );
}

export default App;
