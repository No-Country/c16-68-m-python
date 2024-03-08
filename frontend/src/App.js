import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom'; 
import RegisterForm from './components/Register/RegisterForm';
import LoginForm from './components/Login/LoginForm';
import RastreoEmociones from './pages/RastreoEmociones';
import PaginaPrincipal from 'components/home-page/PaginaPrincipal';
import RecursosBienestar from 'components/RecursosBienestar/RecursosBienestar';
import {TaskPage} from './pages/TaskPage';
import {CreateTodo} from './components/Checklist/CreateTodo';
import {EditTodo} from './components/Checklist/EditTodo';

function App() {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={
          [
            <PaginaPrincipal>
              <RastreoEmociones></RastreoEmociones>
            </PaginaPrincipal>
          ]
        } />
        <Route path='register' element={<RegisterForm/>} />
        <Route path='login' element={<LoginForm/>} />

        <Route path='emotions' element={<RastreoEmociones></RastreoEmociones>}></Route>
        <Route path='recursos/bienestar' element={<RecursosBienestar></RecursosBienestar>}></Route>
        <Route path='tasklist' element={<TaskPage />}></Route>
        {/* <Route path='tasklist/create' element={<CreateTodo />}></Route>
        <Route path='tasklist/taskListView' element={<EditTodo />}></Route> */}
      </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
