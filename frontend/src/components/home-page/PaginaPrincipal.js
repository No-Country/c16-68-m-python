import React from 'react'; 
import HeaderComponent from './HeaderComponent';
import MainComponent from './MainComponent';
import Hero from './Hero'
import Footer from './Footer';




function PaginaPrincipal({children}) {

    return (
      
        <>  
            <div className="b-content">
            <HeaderComponent/>
            <Hero></Hero>
                {<MainComponent/> || children}
            <Footer></Footer>
            </div>
           
        </>
       
       
    );
  
  } 
  
  export default PaginaPrincipal; 
