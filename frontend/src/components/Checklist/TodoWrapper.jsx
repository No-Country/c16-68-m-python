import React from 'react'
import { TodoNav } from './TodoNav'
import { WrapperContent } from './WrapperContent'
import 'bootstrap/dist/css/bootstrap.css'
import './css/checklist.css';

export const TodoWrapper = ({children}) =>{
    return (
        <div id="todoWrapper" className='todoWrapper'>
            {children}
        </div>
    )
}