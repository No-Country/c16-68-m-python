import { useEffect, useState } from 'react';
import Card from 'components/RastreoEmociones/Card';
import Axios from 'axios'
import CurrentDateFormatted from 'utils/CurrentDateFormatted'
import 'bootstrap/dist/css/bootstrap.css'
import { useAuth } from 'context/AuthContext';

const RastreoEmociones = () => {
    const [Emociones,setEmociones] = useState([])
    const {authToken} = useAuth()

    useEffect(()=>{
        (async function (){
            try {
                const axiosRes = await Axios.get('http://127.0.0.1:8000/emotion/emotions/',{
                    headers:{
                        "Content-Type":'application/json',
                        "Authorization" : `Bearer ${authToken}` 
                    }
                })
                console.log(axiosRes.data?.emotions)
                setEmociones(axiosRes.data?.emotions)
            } catch (error) {
                console.error(error)
            }
        })();
    },[])

    return (
        
            <div className='d-flex flex-column gap-2 p-4 w-100 justify-content-center align-items-center '>
                <Card title='¿Como te sientes hoy?' current_date={<CurrentDateFormatted />} emotions={Emociones}></Card>
            </div>
    );
}
 
export default RastreoEmociones;