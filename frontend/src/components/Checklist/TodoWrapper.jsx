import React from 'react'
import { TodoNav } from './TodoNav'
import { WrapperContent } from './WrapperContent'
import 'bootstrap/dist/css/bootstrap.css'

export const TodoWrapper = ({children}) =>{
    return (
        <div id="todoWrapper" className='data-'>
            {children}
        </div>
    )
}