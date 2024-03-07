import {FC, useEffect} from 'react';

import {useAppDispatch, useAppSelector} from "../../hooks";
import {pictureActions} from "../../redux/slices";
import {Picture} from "./Picture";

const Pictures: FC = () => {
    const {pictures} = useAppSelector(state => state.pictures);
    const dispatch = useAppDispatch();
    console.log(pictures)
    useEffect(() => {
        dispatch(pictureActions.getAll())
    }, [dispatch]);

    return (
        <div>
            Pictures
            {pictures.map(picture => <Picture key={picture.id} picture={picture}/>)}
        </div>
    );
};

export {Pictures};