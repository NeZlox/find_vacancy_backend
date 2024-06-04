import { useDispatch, useSelector } from "react-redux";
import Modal from "..";
import { setActive } from "../../../store/slices/modalSlice";
import { Transition } from "react-transition-group";

const ParseModal = () => {
    const dispatch = useDispatch();
    const active = useSelector(state => state.modal.active);

    return ( 
        <Transition in={active} timeout={300} unmountOnExit={true}>
            {(state) => (
                <Modal active={state} setActive={() => dispatch(setActive())}>
                    <h1 className="modal__title">Парсинг вакансий</h1>
                    <div className="input__block">
                        <h1 className="input__block__title">Страна</h1>
                        <input type="text" placeholder="Введите страну..." className="input__block__text" />
                    </div>
                    <div className="input__block">
                        <h1 className="input__block__title">Строка по парсингу</h1>
                        <input type="text" placeholder="Введите строку..." className="input__block__text" />
                    </div>
                    <div className="input__block">
                        <h1 className="input__block__title">Начальная страница</h1>
                        <input type="number" placeholder="Введите начальную страницу..." className="input__block__text" />
                    </div>
                    <div className="input__block">
                        <h1 className="input__block__title">Конечная страница</h1>
                        <input type="number" placeholder="Введите конечную страницу..." className="input__block__text" />
                    </div>

                    <h1 className="modal__parse">Запарсить</h1>
                </Modal>
            )}
        </Transition>
        
     );
}
 
export default ParseModal;