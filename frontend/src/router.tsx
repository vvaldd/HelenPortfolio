import {createBrowserRouter, Navigate} from "react-router-dom";
import {MainLayout} from "./layouts";
import PicturesPage from "./pages/pictures/PicturesPage";


const router = createBrowserRouter([
    {path: '', element: <MainLayout/>, children:[
            {index:true, element:<Navigate to={'pictures'}/>},
            {path:'pictures', element:<PicturesPage/>}
        ]},
])

export {router}