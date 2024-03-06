import React from 'react'; 
import logo from './image/LogoBrain-redim.png';
import './css/menu.css';
import menu from './image/menu-hamburguesa.png';
import { useNavigate, useLocation } from 'react-router-dom';


function Navbar() {
  
  const location = useLocation()

  const isIndexPage = location.pathname === '/'
  const isLogged = localStorage.getItem('token') !== undefined

  const navigate = useNavigate()

  return (
   <> 

      <img src={logo} alt="logo" className="img-logo" />

      <input type="checkbox" id="menu-bar" />
      <label for="menu-bar" ><img src={menu} alt="menu" className="img-label" /></label>

      <nav className="menu">
        <a role='button' onClick={() => navigate('/')} className="margin-right m-t">Inicio</a>
        {
          isIndexPage ? 
            <>
              <a href='' className="margin-right">Nosotros</a>
              <a href='#recursos' className="margin-right">Recursos</a>
              <a href='#contacto' className="margin-right">Contacto</a>
            </> : <></>
        }
        {
          isLogged ? 
          <>
            <a role='button' onClick={() => navigate('/dashboard')}>Dashboard</a>
            <a role='button' onClick={() => {localStorage.clear();navigate('/')}}>Logout</a>
          </>
           : 
          <>
            <a onClick={() => navigate('/login')} className="btn margin-right  back-neutral margin-left">Ingresar</a>
            <a onClick={() => navigate('/register')} className="btn  margin-right" >Registrarse</a>
          </>
        }
      </nav>
   </>
 
   );   
 }      
   
 

  



export default Navbar; 