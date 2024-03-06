// ResourceItem.jsx
import React from 'react';

const ResourceItem = ({ title, description, link, image }) => (
    <div className="resource-item card-bienestar">
        <img src={image} alt={title} className="resource-image" />
        <h3>{title}</h3>
        <p>{description}</p>
        <a href={link} target="_blank" rel="noopener noreferrer">Ir al recurso</a>
    </div>
);

export default ResourceItem;
