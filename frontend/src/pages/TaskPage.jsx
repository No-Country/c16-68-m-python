import React from 'react';
import {TodoNav} from 'components/Checklist/TodoNav';
import {CreateTodo} from 'components/Checklist/CreateTodo';
import {EditTodo} from 'components/Checklist/EditTodo';
import {TodoWrapper} from 'components/Checklist/TodoWrapper';
import {WrapperContent} from 'components/Checklist/WrapperContent';



export const TaskPage = () =>{

    
    return (
        <div id="TaskPage" style={{width:"100%", height:"100%"}}>
            <TodoWrapper>
                <TodoNav/>
                <WrapperContent/>
            </TodoWrapper>
        </div>
    )   
}