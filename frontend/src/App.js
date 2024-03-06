import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom'; 
import RegisterForm from './components/Register/RegisterForm';
import LoginForm from './components/Login/LoginForm';
import RastreoEmociones from './pages/RastreoEmociones';
import HeaderComponent from 'components/home-page/HeaderComponent';
import Footer from 'components/home-page/Footer';
import MainComponent from 'components/home-page/MainComponent';
import Dashboard from 'pages/Dashboard';
import ProtectedRoute from 'utils/ProtectedRoute';
import RecursosBienestar from 'pages/RecursosBienestar.page';

function App() {
  const token = localStorage.getItem('token') !== undefined

  return (
    <>
    <BrowserRouter>
      <HeaderComponent/>
      <Routes>
        <Route path='/' element={<MainComponent/>}></Route>
        <Route path='register' element={<RegisterForm/>} />
        <Route path='login' element={<LoginForm/>} />
        
        <Route element={<ProtectedRoute canActivate={token} redirectPath='/login'/>}>
          <Route path='dashboard' element={<Dashboard></Dashboard>}></Route>
          <Route path='dashboard/emociones' element={<RastreoEmociones></RastreoEmociones>}></Route>
          <Route path='dashboard/bienestar' element={<RecursosBienestar/>}></Route>
        </Route>
      
        <Route path='/*' element={<h1>404 page not found</h1>}/>
      </Routes>
      <Footer/>
    </BrowserRouter>
    </>
  );
}

export default App;
