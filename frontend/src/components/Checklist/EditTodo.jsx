import React from 'react'
import './css/checklist.css';
import 'bootstrap/dist/css/bootstrap.css';

export const EditTodo = () =>{
    return (
        <form id="createForm" className="formC" method='post'>
            <div class="form-check">
                <label class="form-check-label" for="flexCheckChecked">
                    Meditación diaria: 
                </label>
                <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" />
            </div>
            <div class="form-check">
                <label class="form-check-label" for="flexCheckChecked">
                    Ejercicio regular
                </label>
                <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" />
            </div>
            <div class="form-check">
                <label class="form-check-label" for="flexCheckChecked">
                    Alimentación balanceada
                </label>
                <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" />
            </div>
            <div class="form-check">
                <label class="form-check-label" for="flexCheckChecked">
                    Sueño de calidad
                </label>
                <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" />
            </div>
            <div class="form-check">
                <label class="form-check-label" for="flexCheckChecked">
                    Tiempo al aire libre
                </label>
                <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" />
            </div>
            <div class="form-check">
                <label class="form-check-label" for="flexCheckChecked">
                    Establecimiento de metas
                </label>
                <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" />
            </div>
            <div class="form-check">
                <label class="form-check-label" for="flexCheckChecked">
                    Lectura
                </label>
                <input class="form-check-input" type="checkbox" value="HELLO" id="flexCheckChecked" />
            </div>
            <button type="submit" class="btn btn-primary">Submit</button> 
        </form>
    )
}