import {createAsyncThunk, createSlice} from "@reduxjs/toolkit";
import {IPicture} from "../../interfaces";
import {pictureService} from "../../services";


interface IState{
    pictures: IPicture[],
}

const initialState: IState = {
    pictures: []
}

const getAll = createAsyncThunk<IPicture[], void>(
    'picturesSlice/getAll',
    async (_, {rejectWithValue})=> {
        try {
            const {data} = await pictureService.getAll()
            return data
        }catch (e) {
            return rejectWithValue(e)
        }
    }
);


const picturesSlice = createSlice({
    name: 'picturesSlice',
    initialState,
    reducers:{},
    extraReducers: builder =>
        builder
            .addCase(getAll.fulfilled, (state, action) => {
                state.pictures = action.payload
            })
})

const {reducer: pictureReducer, actions} = picturesSlice

const pictureActions = {
    ...actions,
    getAll,
}

export {
    pictureReducer,
    pictureActions,
}