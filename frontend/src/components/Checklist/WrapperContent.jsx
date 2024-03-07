import React from 'react';
import './css/wrapperContent.css';
import { CreateTodo } from './CreateTodo';
// let habits = 
//     `<div id="wrapperContenet">
//         <div class="card" style={{width : "10rem;"}}>
//             <img src="" class="card-img-top" alt=""/>
//             <div class="card-body">
//                 <p class="card-text">Cultivar la meditación diaria fomenta la serenidad mental, reduce el estrés y mejora la concentración, brindando equilibrio y bienestar.</p>
//             </div>
//         </div>
//         <div class="card" style={{width: "10rem;"}}>
//             <div class="card-body">
//                 <p class="card-text">Cultivar la meditación diaria fomenta la serenidad mental, reduce el estrés y mejora la concentración, brindando equilibrio y bienestar.</p>
//             </div>
//         </div>
//     </div>`



export const WrapperContent = () =>{
    return (
        <CreateTodo/>
    )
}
        // <div id="wrapperContenet" className="container-lg">
        //     <div class="card" style={{width : "10rem;"}}>
        //         {/* <img src="data:image/jpeg;base64,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" class="card-img-top" alt="MEDITACION"/> */}
        //         <div class="card-body">
        //         <h5 class="card-title">Meditacion</h5>
        //             <p class="card-text">Cultivar la meditación diaria fomenta la serenidad mental, reduce el estrés y mejora la concentración, brindando equilibrio y bienestar.</p>
        //         </div>
        //     </div>
        //     <div class="card" style={{width: "10rem;"}}>
        //         <div class="card-body">
        //             <h5 class="card-title">Meditacion</h5>
        //             <p class="card-text">Cultivar la meditación diaria fomenta la serenidad mental, reduce el estrés y mejora la concentración, brindando equilibrio y bienestar.</p>
        //         </div>
        //     </div>
        //     <div class="card" style={{width: "10rem;"}}>
        //         <div class="card-body">
        //             <h5 class="card-title">Meditacion</h5>
        //             <p class="card-text">Cultivar la meditación diaria fomenta la serenidad mental, reduce el estrés y mejora la concentración, brindando equilibrio y bienestar.</p>
        //         </div>
        //     </div>
        //     <div class="card" style={{width: "10rem;"}}>
        //         <div class="card-body">
        //             <h5 class="card-title">Meditacion</h5>
        //             <p class="card-text">Cultivar la meditación diaria fomenta la serenidad mental, reduce el estrés y mejora la concentración, brindando equilibrio y bienestar.</p>
        //         </div>
        //     </div>
        //     <div class="card" style={{width: "10rem;"}}>
        //         <div class="card-body">
        //             <h5 class="card-title">Meditacion</h5>
        //             <p class="card-text">Cultivar la meditación diaria fomenta la serenidad mental, reduce el estrés y mejora la concentración, brindando equilibrio y bienestar.</p>
        //         </div>
        //     </div>
        //     <div class="card" style={{width: "10rem;"}}>
        //         <div class="card-body">
        //             <h5 class="card-title">Meditacion</h5>
        //             <p class="card-text">Cultivar la meditación diaria fomenta la serenidad mental, reduce el estrés y mejora la concentración, brindando equilibrio y bienestar.</p>
        //         </div>
        //     </div>
        //     <div class="card" style={{width: "10rem;"}}>
        //         <div class="card-body">
        //             <h5 class="card-title">Meditacion</h5>
        //             <p class="card-text">Cultivar la meditación diaria fomenta la serenidad mental, reduce el estrés y mejora la concentración, brindando equilibrio y bienestar.</p>
        //         </div>
        //     </div>
        // </div>