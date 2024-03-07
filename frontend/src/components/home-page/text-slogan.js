import React from "react";
import "./css/text-slogan.css";
import woman from "./image/young-woman-meditating-nature 1.png";
import { useNavigate } from "react-router-dom";
import { useAuth } from "context/AuthContext";


function TextSlogan() {
  const {isLoggIn} = useAuth()
  const navigate = useNavigate()

  return (
    <>
      <div className="section-1">
        <div className="div-t">
          <div className="text-slogan">
            <p className="p1">
              Creemos en la importancia de cuidar tu salud mental tanto como tu
              salud física.
            </p>
            <p className="p2 margin">
              {" "}
              Una pausa está comprometido con tu bienestar emocional y mental.
            </p>
            <p className="margin p3">
              Nuestra misión es proporcionarte herramientas y recursos que te
              ayuden a encontrar equilibrio, paz interior y claridad mental en
              tu vida diaria.
            </p>
          </div>
          <div className="div-btn">
            {
              isLoggIn ? <></> : <button className="btn-c" onClick={() => navigate('/register')}>Comenza ahora</button>
            }
          </div>
        </div>
        <div className="conteiner-person">
          <img src={woman} alt="img-persona" className="img-p" />
        </div>
      </div>
    </>
  );
}

export default TextSlogan;
