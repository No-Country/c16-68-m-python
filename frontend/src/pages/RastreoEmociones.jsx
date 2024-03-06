import { useEffect, useState } from 'react';
import Card from 'components/RastreoEmociones/Card';
import Axios from 'axios'
import CurrentDateFormatted from 'utils/CurrentDateFormatted'
import 'bootstrap/dist/css/bootstrap.css'

const RastreoEmociones = () => {
    const [Emociones,setEmociones] = useState([])

    useEffect(()=>{
        (async function (){
            try {
                const axiosRes = await Axios.get('http://localhost:3001/emociones')
                setEmociones(axiosRes.data)
            } catch (error) {
                console.error(error)
            }
        })();
    },[])

    return (
        <div className='d-flex flex-column gap-2 mt-2 w-100 justify-content-center align-items-center'>
            <Card title='¿Como te sientes hoy?' current_date={<CurrentDateFormatted/>} emotions={Emociones}></Card>
        </div>
    );
}
 
export default RastreoEmociones;