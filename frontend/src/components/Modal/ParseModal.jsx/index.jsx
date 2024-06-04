import { useDispatch, useSelector } from "react-redux";
import Modal from "..";
import { setActive } from "../../../store/slices/modalSlice";
import { Transition } from "react-transition-group";
import useFetching from "../../../hooks/useFetching";
import ApiService from "../../../api/ApiService";
import { useState } from "react";
import messageTrigger from "../../../utils/messageTrigger";

const ParseModal = () => {
    const dispatch = useDispatch();
    const active = useSelector((state) => state.modal.active);

    const [country, setCountry] = useState("");
    const [line, setLine] = useState("");
    const [pageStart, setPageStart] = useState("");
    const [pageEnd, setPageEnd] = useState("");

    const [fetchParse, isParseLoading] = useFetching(async () => {
        const response = ApiService.startParse(
            country,
            line,
            pageStart,
            pageEnd,
        );

        if (!isParseLoading) {
            setActive(false);
            messageTrigger(dispatch, "Успешно", "access", 2000);
        }
    });
    return (
        <Transition in={active} timeout={300} unmountOnExit={true}>
            {(state) => (
                <Modal active={state} setActive={() => dispatch(setActive())}>
                    <h1 className="modal__title">Парсинг вакансий</h1>
                    <div className="input__block">
                        <h1 className="input__block__title">Страна</h1>
                        <input
                            onChange={(e) => setCountry(e.target.value)}
                            value={country}
                            type="text"
                            placeholder="Введите страну..."
                            className="input__block__text"
                        />
                    </div>
                    <div className="input__block">
                        <h1 className="input__block__title">
                            Строка по парсингу
                        </h1>
                        <input
                            onChange={(e) => setLine(e.target.value)}
                            value={line}
                            type="text"
                            placeholder="Введите строку..."
                            className="input__block__text"
                        />
                    </div>
                    <div className="input__block">
                        <h1 className="input__block__title">
                            Начальная страница
                        </h1>
                        <input
                            onChange={(e) => setPageStart(e.target.value)}
                            value={pageStart}
                            type="text"
                            placeholder="Введите начальную страницу..."
                            className="input__block__text"
                        />
                    </div>
                    <div className="input__block">
                        <h1 className="input__block__title">
                            Конечная страница
                        </h1>
                        <input
                            onChange={(e) => setPageEnd(e.target.value)}
                            value={pageEnd}
                            type="text"
                            placeholder="Введите конечную страницу..."
                            className="input__block__text"
                        />
                    </div>

                    <h1 className="modal__parse" onClick={() => fetchParse()}>
                        Запарсить
                    </h1>
                </Modal>
            )}
        </Transition>
    );
};

export default ParseModal;
