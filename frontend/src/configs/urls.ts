const baseURL = 'http://localhost:8888/api/v1'

const pictures = '/pictures'

const urls = {
    pictures: {
        base: pictures,
        byId:(id:number):string=>`${pictures}/${id}`
    }
}

export {
    baseURL,
    urls
}