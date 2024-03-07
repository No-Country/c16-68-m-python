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
                console.log(`IN USEEFFECT`)
                console.log(r.data)
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

    if (loading){
        return(
            <h1>LOADING</h1>
        )
    }

    return (
        <div id="TaskPage" style={{width:"100%", height:"100%"}}>
            <TodoWrapper>
                <TodoNav/>
                {/* <WrapperContent habitslist={<Tasklist data={habits}/>}/> */}
                <Tasklist data={habits}/>
            </TodoWrapper>
        </div>
    )   
}