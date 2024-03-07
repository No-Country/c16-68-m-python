import React from "react";
import "./css/cards.css";

function Cards(props) {
  return (
    <div id="card" onClick={props.onClick}>
      <div className="img-card">
        <img src={props.img} className="img-card" alt="imagen plan" />
      </div>

      <div className="description">
        <h2 className="title-card">{props.titulo}</h2>
        <p className="desc-card">{props.desc1}</p>
        <p className="desc-card">{props.desc2}</p>
      </div>
    </div>
  );
}

export default Cards;
