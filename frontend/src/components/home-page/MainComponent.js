import React from "react";
import TextSlogan from "./text-slogan";
import Cards from "./Cards";
import FormContact from "./form-contact";
import Reviews from "./Reviews";
import picplan1 from "./image/pic-plan1.png";
import picplan2 from "./image/pic-plan2.png";
import picplan3 from "./image/pic-plan3.png";
import "./css/menu.css";
import "./css/button.css";
import Hero from './Hero'

function MainComponent() {
  return (
    <main>
    <Hero></Hero>
    <TextSlogan />
      <div className="section-2" id="recursos">
        <div className="container-cards">
          <Cards
            className="margin-t"
            img={picplan1}
            titulo="Diario de emociones"
            desc1="Lleva tu diario de"
            desc2="emociones."
          />

          <Cards
            img={picplan2}
            titulo="Hábitos saludables"
            desc1="Hábitos para mejor tu dia a"
            desc2="dia."
          />

          <Cards
            img={picplan3}
            titulo="Recursos bienestar"
            desc1="Artículos escritos por"
            desc2="expertos."
          />
        </div>
      </div>

      <div className="section-4">
        <div >
          <h2 className="title-rev">¿Qué opinan de nosotros?</h2>
        </div>
        <Reviews/>
      </div>

      <FormContact/>
    </main>
  );
}

export default MainComponent;
