import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom'; 
import RegisterForm from './components/Register/RegisterForm';
import LoginForm from './components/Login/LoginForm';
import RastreoEmociones from './pages/RastreoEmociones';
import PaginaPrincipal from 'components/home-page/PaginaPrincipal';
import RecursosBienestar from 'components/RecursosBienestar/RecursosBienestar';

function App() {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={
          [
            <PaginaPrincipal>
              <RastreoEmociones></RastreoEmociones>
            </PaginaPrincipal>
          ]
        } />
        <Route path='register' element={<RegisterForm/>} />
        <Route path='login' element={<LoginForm/>} />

        <Route path='emotions' element={<RastreoEmociones></RastreoEmociones>}></Route>
        <Route path='recursos/bienestar' element={<RecursosBienestar></RecursosBienestar>}></Route>
      </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
