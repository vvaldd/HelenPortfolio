import {FC} from 'react';
import {Header} from "../componets/Header";
import {Outlet} from "react-router-dom";

const MainLayout:FC = () => {
    return (
        <div>
            <Header/>
            <Outlet/>
        </div>
    );
};

export {MainLayout};