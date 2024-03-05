// Footer.jsx
import React from 'react';
import logo from '../images/logo.png'; 
import instagram from '../images/instagram.png';
const Footer = () => (
<footer className="footer">
<div className="footer-content">
    <div className="footer-logo">
    <img src={logo} alt="Logo" height="50" /> 
    </div>
    <div className="footer-links">
    <a href="#inicio">Inicio</a>
    <a href="#nosotros">Nosotros</a>
    <a href="#recursos">Recursos</a>
    <a href="#contactos">Contactos</a>
    </div>
    <div className="footer-social">
    {/* Enlaces a redes sociales */}
        <img src={instagram} alt="instagram" height="50" /> 
    <a href="https://www.facebook.com" target="_blank" rel="noopener noreferrer">
        <img src="Recursos/src/images/facebook.png" alt="Facebook" height="30" />
    </a>
    </div>
</div>
<p className="footer-copyright">
    © Copyright 2024 - Derechos reservados
</p>
</footer>
);

export default Footer;


