import React from "react";
//              ({ Descripcion })
//              -cambiar contraseña
//              -cerrar sesion
//
const Profile = () => {
  return (
    <>
      <link
        href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
        rel="stylesheet"
      />
      <section id="about-section" class="pt-5 pb-5">
        <div class="container wrapabout">
          <div class="red"></div>
          <div class="row">
            <div class="container">
              <div class="col-lg-5 p-5">
                <figure class="potoaboutwrap">
                  <img
                    class="img-fluid img-thumbnail"
                    src="https://images.ctfassets.net/h6goo9gw1hh6/2sNZtFAWOdP1lmQ33VwRN3/24e953b920a9cd0ff2e1d587742a2472/1-intro-photo-final.jpg?w=1200&h=992&q=70&fm=webp"
                    alt="photoabout"
                  />
                </figure>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-lg-6 align-items-center justify-content-left d-flex mb-5 mb-lg-0">
              <div class="blockabout">
                <div class="blockabout-inner text-center text-sm-start">
                  <div class="title-big pb-3 mb-3">
                    <h3>Mi Perfil</h3>
                  </div>
                  <p class="description-p text-muted pe-0 pe-lg-0">
                    Este es mi perfil en Una Pausa
                  </p>
                  <p class="description-p text-muted pe-0 pe-lg-0">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Natus quas optio reiciendis deleniti voluptatem facere.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Profile;
