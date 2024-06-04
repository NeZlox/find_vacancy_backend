import Header from "../components/Header";
import ParseModal from "../components/Modal/ParseModal.jsx";
import VacancyList from "../components/VacancyList";

const FindPage = () => {
    return ( 
        <div className="find_page">
            <Header />
            <VacancyList />
            <ParseModal />
        </div>
     );
}
 
export default FindPage;