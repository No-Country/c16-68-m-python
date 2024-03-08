import React from 'react'
import './css/checklist.css';
import 'bootstrap/dist/css/bootstrap.css';


export const Tasklist = (props) => {
    return (
        <div id="taskList">
            <h2>Habitos Saludables</h2>
            <div style={{ width: "fit-content", height: "fit-content", textAlign:"center"}} className="row justify-content-center align-items-center">
                {props.data.map(element => (
                    <div key={element.id} style={{ width: "fit-content", height: "fit-content"}} className="col-sm-6 col-lg-4">
                        <div className="card" style={{ width: "20rem", height: "13rem"}}>
                            <div className="card-body">
                                <h5 className="card-title">{element.habit_name}</h5>
                                <p className="card-text">{element.description}</p>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};
