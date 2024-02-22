import Emocion from '../../assets/RastreoEmociones/Frame.png'
import Emocion1 from '../../assets/RastreoEmociones/Frame1.png'
import Emocion2 from '../../assets/RastreoEmociones/Frame2.png'

import {format} from 'date-fns'
import {es} from 'date-fns/locale'

import { useState } from 'react'
import { createPortal } from 'react-dom';

import './index.css'
import Modal from './Modal'

const Card = ({titulo,fechaActual,Emociones}) => {
    const fecha = new Date()
    const fechaFormateada = format(fecha, "dd MMM yyyy",{locale: es});
    
    const [showModal, setShowModal] = useState(false);
    return (
        <div style={{display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'space-evenly',
            gap:'2rem',background:'#FFDD6D',borderRadius:'1rem',width:'712px',height:'409px',textAlign:'center'}}>
            <div>
                <h1>¿Cómo te sientes hoy?</h1>
                <h3 style={{textTransform:'capitalize'}}>{fechaFormateada}</h3>
            </div>
            <ul style={{display:'flex', gap:'2rem'}}>
                <li className='list-unstyled' role='button' onClick={() => setShowModal(true)}><img src={Emocion} alt="frame"/></li>
                <li className='list-unstyled' role='button' onClick={() => setShowModal(true)}><img src={Emocion1} alt="frame"/></li>
                <li className='list-unstyled' role='button' onClick={() => setShowModal(true)}><img src={Emocion2} alt="frame"/></li>
            </ul>
            {
                showModal && createPortal(
                    <Modal onClose={() => setShowModal(false)}></Modal>
                    , document.getElementById('portal')
                )
            }
        </div>
    );
}
 
export default Card;