import React from "react";
import "./css/form-contact.css";
import imgcontacto from "./image/3969587 1.png";
import "./css/button.css"

function FormContact() {
  return (
    <div className="section-3" id="contacto">
      <div className="title-contact">
        <h1>¿Tenes alguna sugerencia? ¡Comunícate con nosotros!</h1>
      </div>

      <div className="div-img-contact">
        <img
          src={imgcontacto}
          alt="imagen-chica-oficina"
          className="img-contact"
        />
      </div>

      <div className="form-contact">
        <input
          type="text"
          placeholder="Nombre"
          className="form-name"
        />
        <input
          type="text"
          placeholder="Correo electronico"
          className="form-email margin-t"
        />
        <textarea
          name="mensaje"
          id=""
          cols="30"
          rows="10"
          className="form-msj"
          placeholder="Mensaje"
        />
        <button className="btn-e right">Enviar mensaje</button>
      </div>
    </div>
  );
}

export default FormContact;
