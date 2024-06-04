import { showMessage,clearMessage } from "../store/slices/messageSlice";

const messageTrigger = (dispatch,message,status,timeout) => {
    dispatch(showMessage([message,status]));
    setTimeout(() => {
        dispatch(clearMessage());
    },timeout);
}

export default messageTrigger;