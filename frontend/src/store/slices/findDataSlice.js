import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    text: "",
    fetch: false,
};

export const findDataSlice = createSlice({
    name: 'findData',
    initialState,
    reducers: {
        changeText: (state, action) => {
            state.text = action.payload;
        },
        setFetch: (state, action) => {
            state.fetch = action.payload;
        }
    },
});

export const { changeText,setFetch } = findDataSlice.actions;

export default findDataSlice.reducer;