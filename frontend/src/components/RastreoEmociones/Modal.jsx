import './css/modal.css'
import { useContext, useState } from 'react';
import {EmocionesContext} from 'context/Emociones.context'
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';
import { useAuth } from 'context/AuthContext';
import Swal from 'sweetalert2';
import {useNavigate } from 'react-router-dom';

const Modal = ({onClose}) => {
    
    const {authToken,setIsLoggIn} = useAuth()
    const emocion = useContext(EmocionesContext)
    const [description,setDescription] = useState('')

    const navigate = useNavigate()
    
    const jwt = jwtDecode(authToken)

    const Toast = Swal.mixin({
        toast: true,
        position: 'top',
        iconColor: 'green',
        customClass: {
          popup: 'colored-toast',
        },
        showConfirmButton: false,
        timer: 4000,
        timerProgressBar: true,
      })

    const HandleSubmit = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:8000/emotion/emotion_logs/',{
                "id":jwt.user_id,
                "emotion":emocion.emotion_name,
                "description": description
            },{
                headers:{
                    "Content-Type":'application/json',
                    "Authorization" : `Bearer ${authToken}` 
                }
            })
            console.log(response)
            if(response.status === 200){
                Toast.fire({
                    icon: 'success',
                    title: 'Emocion Guardada!',
                })
                onClose()
            }
        } catch (error) {
            if(error.response?.status === 400){
                Swal.fire({
                    title:'La sesion a expirado...',
                    icon:'error'
                }).then((res) => {
                    if(res.isConfirmed){
                        setIsLoggIn(false)
                        navigate('/login')
                    }
                })
                
            }else if(error.response?.status === 401){
                Swal.fire({
                    title:'No autorizado',
                    icon:'error'
                }).then((res) => {
                    if(res.isConfirmed){
                        setIsLoggIn(false)
                        navigate('/login')
                    }
                })
            }
        }

    }
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
                     placeholder='Hoy me siento...' onChange={(e) => {setDescription(e.target.value)}}></textarea>
                </div>
                <footer className='modal-footer d-flex justify-content-between gap-3 w-100 mt-2'>
                    <button className="btn-modal" onClick={onClose}>Cancelar</button>
                    <button type='submit' className="btn-modal" onClick={HandleSubmit}>Guardar</button>
                </footer>
            </article>
        </>
    );
}
 
export default Modal;