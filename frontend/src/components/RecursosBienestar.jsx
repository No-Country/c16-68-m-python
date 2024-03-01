// RecursosBienestar.jsx
import React from 'react';
import ResourceItem from './ResourceItem';

const RecursosBienestar = ({ resources }) => {
return (
<div className="resources-container">
    {resources.map((resource, index) => (
    <ResourceItem key={index} {...resource} />
    ))}
</div>
);
};

export default RecursosBienestar;

