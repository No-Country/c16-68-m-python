// Card.jsx
import React from 'react';

const Card = ({ title, description, link }) => (
    <div className="card">
        <h3 className='title'>{title}</h3>
        <p>{description}</p>
        <a href={link} target="_blank" rel="noopener noreferrer">Ir al recurso</a>
    </div>
);

export default Card;

