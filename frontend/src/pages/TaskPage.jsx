import React from 'react';
import {TodoNav} from 'components/Checklist/TodoNav';
import {CreateTodo} from 'components/Checklist/CreateTodo';
import {TodoWrapper} from 'components/Checklist/TodoWrapper';
import {EditTodo} from 'components/Checklist/EditTodo';
import {Tasklist} from 'components/Checklist/Tasklist';
import {WrapperContent} from 'components/Checklist/WrapperContent';
import { useEffect, useState} from 'react';
import {getAllTask} from '../api/getlist.api'

export const TaskPage = () =>{
    
    const [habits, SetHabits] = useState([])
    const [loading, SetLoading] = useState(true)
    useEffect(() => {
        async function loadTask(){
            try{
                const r = await getAllTask();
                SetHabits(r.data);
            }
            catch(e){
                console.log("error fetching the data", e)
            }
            finally{
                SetLoading(false)
            }
        }
        loadTask();
    }, []);
    console.log(habits)
    
    if (loading){
        return(
            <div className="loader">UnaPausa</div>
            )
        }
    return (
        <div id="TaskPage" style={{ width:"100%", height:"100%" }}>
            <TodoWrapper>
                <TodoNav/>
                <WrapperContent props={<Tasklist data={habits}/>}>
                </WrapperContent>
            </TodoWrapper>
        </div>
    )   
}