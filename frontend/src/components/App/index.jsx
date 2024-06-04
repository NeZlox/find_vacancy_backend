import FindPage from "../../pages/FindPage";
import { Provider } from "react-redux";
import { store } from "../../store/store";
import Message from "../UI/Message";

const App = () => {
    return (
        <Provider store={store}>
            <FindPage />
            <Message />
        </Provider>
    );
};

export default App;
