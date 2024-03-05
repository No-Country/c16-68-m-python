// Navbar.jsx
import React from 'react';
import logo from '../images/logo.png'; // Asegúrate de ajustar la ruta al lugar donde tengas tu imagen de logo

const Navbar = () => (
<nav className="navbar">
<a href="#inicio" className="navbar-logo">
    <img src={logo} alt="Logo" height="50" /> {/* Ajusta el tamaño según necesites */}
</a>
<a href="#inicio">Inicio</a>
<a href="#nosotros">Nosotros</a>
<a href="#recursos">Recursos</a>
<a href="#contactos">Contactos</a>
<a href="#login">Login</a>

</nav>
);

export default Navbar;

