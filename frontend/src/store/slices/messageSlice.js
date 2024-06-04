import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    isActive: false,
    message: null,
    status: null
};

export const messageSlice = createSlice({
    name: "messageData",
    initialState,
    reducers: {
        showMessage: (state, action) => {
            const [message,status] = action.payload;
            state.message = message;
            state.status = status;
            state.isActive = true;
        },
        clearMessage: (state) => {
            state.isActive = false;
        },
    },
});

export const { showMessage, clearMessage } = messageSlice.actions;

export default messageSlice.reducer;
