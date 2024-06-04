import { useEffect, useState } from "react";
import ApiService from "../../api/ApiService";
import useFetching from "../../hooks/useFetching";
import VacancyWorker from "../VacancyWorker";
import { TbFaceIdError } from "react-icons/tb";
import { useDispatch, useSelector } from "react-redux";
import { setFetch } from "../../store/slices/findDataSlice";
import Loader from "../UI/Loader";
import messageTrigger from "../../utils/messageTrigger";

const VacancyList = () => {
    const dispatch = useDispatch();
    const [data,setData] = useState([]);
    const fetch = useSelector(state => state.findData.fetch);
    const text = useSelector(state => state.findData.text);
    
    const [fetchVacancy,isVacancyLoading] = useFetching(async () => {
        const response = await ApiService.getVacancy(text);
        if (!isVacancyLoading) {
            setData(response);
            messageTrigger(dispatch,"Успешно","access",2000);
        }
    });

    useEffect(() => {
        fetchVacancy();
    },[]);

    useEffect(() => {
        if (fetch) {
            dispatch(setFetch(false));
            fetchVacancy();
        }
    },[fetch]);

    return (
        <>
            {isVacancyLoading && <Loader />}
            <section className="vacancy_list">
                <div className="container">
                    <div className="vacancy_list__inner">
                        <h1 className="vacancy_list__title">Результаты поиска:</h1>
                        {data && data.length ? (
                            <div className="vacancy_list__workers">
                                {data.map((worker) => (
                                    <VacancyWorker key={worker.id} worker={worker} />
                                ))}
                            </div>
                        ) : (
                            <div className="vacancy_list__empty">
                                <h1 className="vacancy_list__empty__title">
                                    По данному запросу ничего не найдено
                                </h1>
                                <TbFaceIdError id="icon" />
                            </div>
                        )}
                    </div>
                </div>
            </section>
        </>
        
    );
};

export default VacancyList;
