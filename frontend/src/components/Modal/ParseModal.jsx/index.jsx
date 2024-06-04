import { useDispatch, useSelector } from "react-redux";
import Modal from "..";
import { setActive } from "../../../store/slices/modalSlice";
import { Transition } from "react-transition-group";
import useFetching from "../../../hooks/useFetching";
import ApiService from "../../../api/ApiService";
import { useEffect, useState } from "react";
import messageTrigger from "../../../utils/messageTrigger";

const ParseModal = () => {
    const dispatch = useDispatch();
    const active = useSelector((state) => state.modal.active);

    const [country, setCountry] = useState("moscow");
    const [line, setLine] = useState("");
    const [pageStart, setPageStart] = useState(0);
    const [pageEnd, setPageEnd] = useState(0);
    const [error,setError] = useState("");

    const numberValidate = (side,value) => {
        if (value.length && value[value.length-1] == '.') return;
        if (!isNaN(Number(value))) {
            if (side == "Start") {
                setPageStart(value.length ? Number(value) : "");
            } else {
                setPageEnd(value.length ? Number(value) : "");
            }
        }
    }

    const [fetchParse, isParseLoading] = useFetching(async () => {

        if (!line) {
            setError("Введите строку по парсингу!");
            return;
        }
        if (!pageStart) {
            setError("Введите начальную страницу!");
            return;
        }
        if (!pageEnd) {
            setError("Введите конечную страницу!");
            return;
        }

        if (pageStart > pageEnd) {
            setError("Начальная страница должна быть меньше конечной!");
            return;
        }

        const response = ApiService.startParse(
            country,
            line,
            pageStart,
            pageEnd,
        );

        if (!isParseLoading) {
            dispatch(setActive(false));
            messageTrigger(dispatch, "Успешно", "access", 2000);
        }
    });
   

    const countries = [
        {country:"Москва",abbr:"moscow"},
        {country:"Санкт-Петербург", abbr:"spb"},
        {country:"Волгоград", abbr:"volgograd"},
        {country:"Владивосток", abbr:"vladivostok"},
        {country:"Воронеж", abbr:"voronezh"},
        {country:"Краснодар", abbr:"krasnodar"},
        {country:"Красноярск", abbr:"krasnoyarsk"},
        {country:"Сочи", abbr:"sochi"},
        {country:"Саратов", abbr:"saratov"}
    ];

    useEffect(() => {
        setCountry("moscow");
        setLine("");
        setPageStart("");
        setPageEnd("");
    },[active]);

    return (
        <Transition in={active} timeout={300} unmountOnExit={true}>
            {(state) => (
                <Modal active={state} setActive={() => dispatch(setActive())}>
                    <h1 className="modal__title">Парсинг вакансий</h1>
                    <div className="input__block">
                        <h1 className="input__block__title">Город</h1>
                        <select onChange={(e) => setCountry(e.target.value)} className="input__block__text" >
                            {countries.map(country => (
                                <option value={country.abbr}>{country.country}</option>
                            ))}
                        </select>
                       
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
                            onChange={(e) => numberValidate("Start",e.target.value)}
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
                            onChange={(e) => numberValidate("End",e.target.value)}
                            value={pageEnd}
                            type="text"
                            placeholder="Введите конечную страницу..."
                            className="input__block__text"
                        />
                    </div>

                    <h1 className="modal__parse" onClick={() => fetchParse()}>
                        Запарсить
                    </h1>
                    <h1 className="modal__error">{error}</h1>
                </Modal>
            )}
        </Transition>
    );
};

export default ParseModal;
