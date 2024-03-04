import {apiService, IResponse} from "./api.service";
import {IPicture} from "../interfaces";
import {urls} from "../configs";

const pictureService = {
    getAll:():IResponse<IPicture[]> => apiService.get(urls.pictures.base)
}

export {
    pictureService
}