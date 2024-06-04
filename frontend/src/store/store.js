import { configureStore } from "@reduxjs/toolkit";
import findDataSlice from "./slices/findDataSlice";
import messageSlice from "./slices/messageSlice";
import modalSlice from "./slices/modalSlice";

export const store = configureStore({
    reducer: {
        findData: findDataSlice,
        messageData: messageSlice,
        modal:modalSlice
    }
});