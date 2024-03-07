import React from 'react'
import './css/todoNav.css';


export const TodoNav = () =>{

    function createForm(){
        
    }
    return (
        <div id="TodoNav" className='nav-options'>
            <div className='create-ls'>
                <button className='btn btn-primary'>Crea una lista</button>
            </div>
            <div className='create-ls'> 
                <button onClick={createForm} className='btn btn-primary'>Lista de hoy</button>
            </div>
        </div>
    )
}