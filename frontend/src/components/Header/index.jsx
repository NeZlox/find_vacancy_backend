import Title from "../UI/Title";
import { MdOutlineFindInPage } from "../../utils/icons";
import { MdFindReplace } from "react-icons/md";
import Input from "../UI/Input";
import { useDispatch } from "react-redux";
import { setActive } from "../../store/slices/modalSlice";

const Header = () => {
    const dispatch = useDispatch();
    return (
        <header className="header">
            <div className="container">
                <div className="header__inner">
                    <Title
                        className={"header__title"}
                        icon={<MdOutlineFindInPage id="icon" />}
                    >
                        Поиск вакансий
                    </Title>
                    <Input />
                    <Title
                        onClick={() => dispatch(setActive(true))}
                        className={"header__parse"}
                        icon={<MdFindReplace id="icon" />}
                       
                    >
                        Парсинг вакансий
                    </Title>
                </div>
            </div>
        </header>
    );
};

export default Header;
