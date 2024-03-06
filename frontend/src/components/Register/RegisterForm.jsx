import {useState} from 'react';
import {useNavigate} from 'react-router-dom'
import axios from 'axios'
import Swal from 'sweetalert2'
import 'bootstrap/dist/css/bootstrap.css'

const RegisterForm = () => {
    const [username,setUsername] = useState()
    const [email,setEmail] = useState()
    const [password,setPassword] = useState()

    const navigate = useNavigate()
  
    const HandleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/accounts/create/',{
                "email": email,
                "username": username,
                "password": password
              })
            if(response.status === 201){
                Swal.fire({
                    title: 'Registrado Correctamente!',
                    icon: 'success'
                }).then((resp) => {
                    if (resp.isConfirmed){
                        navigate('/login')
                    }
                })
            }else{
                Swal.fire({
                    title:'Erorr',
                    icon:'error'
                })
            }
        } catch (error) {
            console.error(error)
        }
    }

    return (
        <div className="app vh-100 d-flex flex-column justify-content-center align-items-center">
            <div className='bg-white rounded-3 gap-3 d-flex flex-column justify-content-center align-items-center p-4' style={{ width: '536px', minHeight: '287px' }}>
                <h3 className='text-center'>Registrate</h3>
                <form className='w-75' onSubmit={HandleSubmit}>
                    <div className="mb-3">
                        <label htmlFor="email" className="form-label">Email</label>
                        <input type="email" className="form-control" placeholder='Ingresa tu email' required id="email" onChange={(e) => { setEmail(e.target.value) }} />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="username" className="form-label">Usuario</label>
                        <input type="text" className="form-control" placeholder='Ingresa un usuario' required id="username" onChange={(e) => { setUsername(e.target.value) }} />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="password" className="form-label">Contraseña</label>
                        <input type="password" className="form-control" placeholder='Ingresa una contraseña' required id="password" onChange={(e) => { setPassword(e.target.value) }} />
                    </div>
                    <button type="submit" className="btn mt-3 w-100" style={{ backgroundColor: '#20C95D' }}>Registrarse</button>
                </form>
                <p><a role='button' className='link' onClick={() => navigate('/login')}>¿Ya tienes cuenta?</a></p>
            </div>
        </div>
    );
}
 
export default RegisterForm