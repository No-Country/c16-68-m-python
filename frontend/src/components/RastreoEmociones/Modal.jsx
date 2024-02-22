import Emocion from '../../assets/RastreoEmociones/Frame.png'
import './index.css'

const Modal = ({onClose}) => {
    return (
        <>
            <div className='overlay'/>
            <article className='popup' style={{ marginBottom: '2rem', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', width: '332px', height: '483px', borderRadius: '1rem', background: 'rgb(255, 221, 109)' }}>
                <div style={{ marginBottom: '.5rem', display: 'flex', alignItems: 'center', justifyContent: 'space-evenly', flexDirection: 'column', width: '270px', height: '396px', background: 'white', borderRadius: '1rem', border: '1px solid black' }}>
                    <div className='text-center d-flex flex-column gap-2'>
                        <picture><img src={Emocion} alt="frame"></img></picture>
                        <h3>Contento</h3>
                    </div>
                    <textarea className='border-0 p-2' rows='4' cols='25' maxLength='100'
                     placeholder='Hoy me siento contento, ya que logre mi objetivo del mes...'></textarea>
                </div>
                <footer style={{ display: 'flex', justifyContent: 'space-between', gap: '1rem', maxWidth: '270px', width: '100%', marginTop: '.5rem' }}>
                    <button className="btn-modal" onClick={onClose}>Cancelar</button>
                    <button className="btn-modal">Guardar</button>
                </footer>
            </article>
        </>
    );
}
 
export default Modal;