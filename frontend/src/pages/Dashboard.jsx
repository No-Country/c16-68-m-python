import Cards from "components/home-page/Cards";
import picplan1 from "../components/home-page/image/pic-plan1.png";
import picplan2 from "../components/home-page/image/pic-plan2.png";
import picplan3 from "../components/home-page/image/pic-plan3.png";
import '../components/home-page/css/cards.css'
import { useNavigate } from "react-router-dom";

const Dashboard = () => {

    const navigate = useNavigate()

    return (
        <section className="text-center gap-3 m-4 d-flex flex-column">
            <h1>Nuestros Recursos</h1>
            <div className="container-cards">
                <Cards
                    className="margin-t"
                    img={picplan1}
                    titulo="Diario de emociones"
                    desc1="Lleva tu diario de"
                    desc2="emociones."
                    onClick={() => navigate('emociones')}
                />

                <Cards
                    img={picplan2}
                    titulo="Hábitos saludables"
                    desc1="Hábitos para mejor tu dia a"
                    desc2="dia."
                    onClick={() => alert('Habitos Saludables')}
                />

                <Cards
                    img={picplan3}
                    titulo="Recursos bienestar"
                    desc1="Artículos escritos por"
                    desc2="expertos."
                    onClick={() => navigate('bienestar')}
                />
            </div>
        </section>
    );
}
 
export default Dashboard;