import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom'; 
import { useAuth } from 'context/AuthContext';

import HeaderComponent from 'components/home-page/HeaderComponent';
import Footer from 'components/home-page/Footer';
import ProtectedRoute from 'utils/ProtectedRoute';
import MainComponent from 'components/home-page/MainComponent';
import Dashboard from 'pages/Dashboard';
import BienestarPage from 'pages/BienestarPage';
import LoginForm from './components/Login/LoginForm';
import RegisterForm from'./components/Register/RegisterForm';
import RastreoEmociones from'./pages/RastreoEmociones';


function App() {
  const {isLoggIn} = useAuth()

  return (
    <>
      <BrowserRouter>
          <HeaderComponent />
          <Routes>
            <Route path='/' element={<MainComponent />}></Route>
            <Route path='register' element={<RegisterForm />} />
            <Route path='login' element={<LoginForm />} />

            <Route element={<ProtectedRoute canActivate={isLoggIn} redirectPath='/login' />}>
              <Route path='dashboard' element={<Dashboard></Dashboard>}></Route>
              <Route path='dashboard/emociones' element={<RastreoEmociones></RastreoEmociones>}></Route>
              <Route path='dashboard/bienestar' element={<BienestarPage />}></Route>
            </Route>

            <Route path='/*' element={<h1>404 page not found</h1>} />
          </Routes>
          <Footer />
      </BrowserRouter>
    </>
  );
}

export default App;
