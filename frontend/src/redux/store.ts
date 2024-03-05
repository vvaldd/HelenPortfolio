import {configureStore} from "@reduxjs/toolkit";
import {pictureReducer} from "./slices";


const store = configureStore({
    reducer:{
        pictures: pictureReducer,
    },
})

type RootState = ReturnType<typeof store.getState>

type AppDispatch = typeof store.dispatch

export {store}

export type {
    RootState,
    AppDispatch,
}