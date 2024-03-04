import axios, {AxiosResponse} from "axios";
import {baseURL} from "../configs";

type IResponse<T> = Promise<AxiosResponse<T>>

const apiService = axios.create({baseURL});

export {
    apiService
}

export type {
    IResponse
}