import React from "react";
import "./css/reviews.css";
import perfil2 from "./image/perfil2.png";
import perfil1 from "./image/perfil1.png";
import perfil3 from "./image/perfil3.png";


function Reviews() {
  return (
    <>
      <div className="reviews">
        <div className="rev-1">
          <div className="header-rev">
            <div className="img-rev">
              <img src={perfil2} alt="usuario" className="img-user" />
            </div>

            <div className="name">
              <h2 className="name-user">Paola Flores</h2>
            </div>
          </div>
          <div className="review">
            <p className="text-review">
              Esta página ha sido una herramienta increíble para mí! Me ayuda a
              identificar mis emociones y a comprender mejor cómo me siento en
              diferentes situaciones. El diseño es muy fácil de usar y el
              historial de emociones me permite hacer un seguimiento de mi
              progreso.{" "}
            </p>
          </div>
        </div>

        <div className="rev-2">
          <div className="header-rev">
            <div className="img-rev">
              <img src={perfil1} alt="usuario" className="img-user" />
            </div>
            <div className="name">
              <h2 className="name-user">Rodrigo Garcia </h2>
            </div>
          </div>
          <div className="review">
            <p className="text-review">
              Estoy impresionado por lo útil que es esta página. Me ha ayudado a
              tomar conciencia de mis emociones y a encontrar formas saludables
              de manejar el estrés. El diseño es limpio y simple, lo que hace
              que sea fácil de usar. ¡Gracias por crear una herramienta tan
              valiosa para cuidar de nuestra salud mental
            </p>
          </div>
        </div>

        <div className="rev-3">
          <div className="header-rev">
            <div className="img-rev">
              <img src={perfil3} alt="usuario" className="img-user" />
            </div>
            <div className="name">
              <h2 className="name-user">Juan Perez</h2>
            </div>
          </div>
          <div className="review">
            <p className="text-review">
              Desde que descubrí esta app, se ha convertido en una parte
              esencial de mi rutina diaria. La simplicidad de su diseño y la
              claridad de su enfoque me atrajeron desde el principio. Al usarla,
              me he dado cuenta de cuánto influyen mis emociones en mi bienestar
              general.
            </p>
          </div>
        </div>
      </div>
    </>
  );
}

export default Reviews;
