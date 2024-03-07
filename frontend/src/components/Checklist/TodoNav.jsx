import React from 'react'
import './css/todoNav.css';


export const TodoNav = () =>{
    return (
        <div id="TodoNav" className='nav-options'>
            <div className='create-ls'>
                <button className='btn btn-primary'>Crea una lista</button>
            </div>
            <div className='create-ls'> 
                <button className='btn btn-primary'>Lista de hoy</button>
            </div>
        </div>
    )
}