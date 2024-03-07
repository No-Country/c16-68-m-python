// RecursosBienestar.jsx
import React from 'react';
import ResourceItem from './ResourceItem';
import './css/RecursosBienestar.css'

import stres from './images/stres.png'
import meditar from './images/meditar.png'
import dormir from './images/dormir.png'
import relajacion from './images/relajacion.png'

const RecursosBienestar = () => {
    const resources = [
        {
          title: 'Cómo Manejar el Estrés',
          description: 'Consejos prácticos para manejar el estrés en la vida diaria.',
          link: 'https://encr.pw/P2Wc2',
          image: stres, 
        },
        {
          title: 'Meditación Guiada para la Paz Interior',
          description: 'Una meditación guiada para encontrar la paz interior y la calma.',
          link: 'https://l1nq.com/YxHHZ',
          image: meditar, 
        },
        {
          title: 'Ejercicios de Respiración Profunda',
          description: 'Aprende técnicas de respiración profunda para reducir la ansiedad.',
          link: 'https://acesse.one/EwACG',
          image: relajacion,
        },
        {
          title: 'Consejos para un Sueño Mejor',
          description: 'Descubre hábitos y consejos para mejorar la calidad del sueño.',
          link: 'https://l1nk.dev/rFoOw',
          image: dormir, 
        }
      ];

    return (
    <div className="resources-container">
        {
          resources.map((resource, index) => (
            <ResourceItem key={index} {...resource} />
          ))
        }
    </div>
    );
};

export default RecursosBienestar;

