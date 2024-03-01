// App.js o App.jsx
import React, { useState } from 'react';
import Navbar from './Navbar';
import Footer from './Footer';
import RecursosBienestar from './RecursosBienestar';
import './App.css'; 

function App() {
  const [resources] = useState([
    {
      title: 'Cómo Manejar el Estrés',
      description: 'Consejos prácticos para manejar el estrés en la vida diaria.',
      link: 'https://encr.pw/P2Wc2',
      image: '/images/stres.png', 
    },
    {
      title: 'Meditación Guiada para la Paz Interior',
      description: 'Una meditación guiada para encontrar la paz interior y la calma.',
      link: 'https://l1nq.com/YxHHZ',
      image: '/images/meditar.png', 
    },
    {
      title: 'Ejercicios de Respiración Profunda',
      description: 'Aprende técnicas de respiración profunda para reducir la ansiedad.',
      link: 'https://acesse.one/EwACG',
      image: '/images/relajacion.png',
    },
    {
      title: 'Consejos para un Sueño Mejor',
      description: 'Descubre hábitos y consejos para mejorar la calidad del sueño.',
      link: 'https://l1nk.dev/rFoOw',
      image: '/images/dormir.png', 
    },
  ]);

  return (
    <div className="app">
      <Navbar />
      <h1>Recursos de Bienestar</h1>
      <RecursosBienestar resources={resources} />
      <Footer />
    </div>
  );
}

export default App;


