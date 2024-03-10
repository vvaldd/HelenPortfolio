import {FC, PropsWithChildren} from 'react';
import {IPicture} from "../../interfaces";

interface IProps extends PropsWithChildren {
    picture: IPicture
}

const Picture: FC<IProps> = ({picture}) => {
    const {id, title, format, genre, image} = picture
    return (
        <div>
            <div>id: {id}</div>
            <div>title: {title}</div>
            <div>format: {format}</div>
            <div>genre: {genre}</div>
            <img
                src={image}
                alt={title}
            />
        </div>
    );
};

export {Picture};