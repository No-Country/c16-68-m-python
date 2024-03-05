import React from 'react'; 
import logo from './image/LogoBrain-redim.png';
import './css/menu.css';
import menu from './image/menu-hamburguesa.png';


function Navbar() {

  return (
   
    <div className="container">
      
        <img src={logo} alt="logo" className="img-logo"/>
      
      <input type="checkbox" id="menu-bar"/>
      <label for="menu-bar" ><img src={menu} alt="menu" className="img-label"/></label>
      
      <nav className="menu">
        
          <a href="" target="_blank" className="margin-right m-t">Inicio</a>
          <a href="" target="_blank" className="margin-right">Nosotros</a>
          <a href="" target="_blank" className="margin-right">Recursos</a>
          <a href="" className="margin-right">Contacto</a>
          <a className="btn margin-right  back-neutral margin-left">Ingresar</a>
          <a className="btn  margin-right" >Registrarse</a>
          
      </nav>

        <div className="text-banner">
            <p className="a1">Tu bienestar, nuestra misión.</p>
           
        </div>
      
    </div>

  

      
   );   
 }      
   
 

  



export default Navbar; 