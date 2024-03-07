import React from 'react'
import './css/todoNav.css';


export const Tasklist = (props) => {
    return (
        <div id="taskList" className="ds-flex">
            {props.data.map(element => (
            <div key={element.id} className="card" style={{ width: "10rem" }}>
                <div className="card-body">
                <h5 className="card-title">{element.habit_name}</h5>
                <p className="card-text">{element.description}</p>
                </div>
            </div>
            ))}
        </div>
    );
};