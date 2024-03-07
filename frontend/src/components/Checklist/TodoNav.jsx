import React from 'react'
import 'bootstrap/dist/css/bootstrap.css';
import './css/checklist.css';


export const TodoNav = () =>{

    function createForm(){
        
    }
    return (
        <div id="TodoNav" className='nav-options'>
            <div className='create-ls'>
                <button className='mybtn'>Crea una lista</button>
            </div>
            <div className='create-ls'> 
                <button onClick={createForm} className='mybtn'>Lista de hoy</button>
            </div>
        </div>
    )
}