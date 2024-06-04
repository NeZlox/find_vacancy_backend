import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    active: false,
};

export const modalSlice = createSlice({
    name: 'findData',
    initialState,
    reducers: {
        setActive: (state, action) => {
            state.active = action.payload;
        }
    },
});

export const { setActive } = modalSlice.actions;

export default modalSlice.reducer;