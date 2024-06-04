import WorkerLink from "../UI/WorkerLink";

const VacancyWorker = ({ worker }) => {
    const { title, salary, experience, work_format, description, url, skills } =
        worker;

    return (
        <div className="vacancy_worker">
            <div className="vacancy_worker__inner">
                <h1 className="vacancy_worker__title">{title}</h1>
                <h1 className="vacancy_worker__subtitle">
                    {salary}
                </h1>
                <div className="vacancy_worker__content">
                    {experience && <h1 className="vacancy_worker__content__item">{experience}</h1>}
                    
                    {work_format && <h1 className="vacancy_worker__content__item">{work_format}</h1>}

                </div>
                <footer className="vacancy_worker__footer">
                    <WorkerLink url={url} />
                </footer>
            </div>
        </div>
    );
};

export default VacancyWorker;
