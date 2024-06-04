import { HiMagnifyingGlass } from "../../utils/icons";
import { IoMdClose } from "../../utils/icons";
import { useDispatch, useSelector } from "react-redux";
import { changeText, setFetch } from "../../store/slices/findDataSlice";
import { useState,useCallback } from "react";

const Input = () => {
    const dispatch = useDispatch();
    const text = useSelector((state) => state.findData.text);
    const [timer, setTimer] = useState(null); 

    const delayedDispatch = useCallback(() => {
        
        setTimer(setTimeout(() => {
            dispatch(setFetch(true));
        }, 1000));
    }, [dispatch]);

    const onChangeTextHandler = (text) => {
        
        dispatch(changeText(text));
        clearTimeout(timer);
        delayedDispatch()
    };

    return (
        <section className="input_block">
            <div className="input_block__icon_inner">
                <HiMagnifyingGlass id="icon" />
            </div>
            <input
                type="text"
                autoComplete="false"
                placeholder="Введите критерий поиска"
                value={text}
                onChange={(event) => onChangeTextHandler(event.target.value)}
                className="input_block__input"
            />
            <div className="input_block__icon_inner close">
                {text && (
                    <IoMdClose
                        onClick={() => dispatch(changeText(""))}
                        id="icon"
                    />
                )}
            </div>
        </section>
    );
};

export default Input;
