import { useSelector } from "react-redux";
import { CSSTransition } from "react-transition-group";
import { useRef } from "react";

const Message = () => {
    const nodeRef = useRef(null);
    const {message,status,isActive} = useSelector(state => state.messageData);
    return ( 
        <CSSTransition
            in={isActive} 
            timeout={300} 
            classNames="fade"
            nodeRef={nodeRef}
            unmountOnExit
        >
            <h1 ref={nodeRef} className={`message ${status}`}>{message}</h1>
        </CSSTransition>
     );
}
 
export default Message;