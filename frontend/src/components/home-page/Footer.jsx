// Footer.jsx
import React from 'react';
import logo from './image/LogoBrain-redim.png'; 
import instagram from './image/instagram.png';
import './css/footer.css'

const Footer = () => {
    return(
        <footer className="footer relative">
            <div className="footer-content mt-3">
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
                </div>
            </div>
            <p className="footer-copyright">
                © Copyright 2024 - Derechos reservados
            </p>
        </footer>
    )
};

export default Footer;


