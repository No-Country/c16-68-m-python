import { useState } from 'react'
import { createPortal } from 'react-dom';
import { EmocionesContext } from 'context/Emociones.context';
import Modal from './Modal'
import './css/card.css'

const Card = ({title,current_date,emotions}) => {

    const [showModal,setShowModal] = useState()

    const [emotion,SetEmocion] = useState(null)
    
    return (
        <div className='d-flex flex-column align-items-center justify-content-evenly gap-3 text-center rounded-4' id='emotioncard'>
            <div>
                <h1 >{title}</h1>
                <h3 className='text-capitalize'>{current_date}</h3>
            </div>
            <ul className='d-flex gap-3 p-0'>
                {
                    emotions.map((emotion) => (
                        <li key={emotion.id} className='list-unstyled' role='button' 
                        onClick={(element) =>{
                            setShowModal(true)
                            SetEmocion({
                                emotion_name : element.target.className,
                                img_url : element.target.src
                            })
                        }}>
                            <img className={emotion.name} src={'http://127.0.0.1:8000/'+emotion.img_emotion} alt="frame"/>
                        </li>
                    ))
                }
            </ul>
            <EmocionesContext.Provider value={emotion}>
                {showModal && createPortal(
                    <Modal onClose={() => setShowModal(false)}></Modal>
                    , document.getElementById('portal')
                )}
            </EmocionesContext.Provider>
        </div>
    );
}
 
export default Card;