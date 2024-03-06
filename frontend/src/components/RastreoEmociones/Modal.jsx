import './css/modal.css'
import { useContext, useState } from 'react';
import {EmocionesContext} from 'context/Emociones.context'

const Modal = ({onClose}) => {
    
    const emocion = useContext(EmocionesContext)
    //const [description,setDescription] = useState()

    return (
        <>
            <div className='overlay'/>
            <article className='popup d-flex flex-column align-items-center justify-content-center rounded-5 h-100' >
                <div className='modal-body d-flex flex-column justify-content-evenly align-items-center mb-2 rounded-4 border border-black border-1'>
                    <div className='text-center d-flex flex-column gap-3'>
                        <picture><img src={emocion.img_url} alt={emocion.emotion_name}></img></picture>
                        <h3>{emocion.emotion_name}</h3>
                    </div>
                    <textarea className='border-0 p-2' rows='4' cols='25' maxLength='100'
                     placeholder='Hoy me siento...'></textarea>
                </div>
                <footer className='modal-footer d-flex justify-content-between gap-3 w-100 mt-2'>
                    <button className="btn-modal" onClick={onClose}>Cancelar</button>
                    <button className="btn-modal" >Guardar</button>
                </footer>
            </article>
        </>
    );
}
 
export default Modal;