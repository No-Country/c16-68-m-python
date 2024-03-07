import axios from 'axios'


export const getAllTask = () => {
    try{
        const resp = axios.get('http://localhost:8000/api/checklist/habits/');
        return resp;
    }
    catch(e){
        console.error('Error:', e);
    }
}