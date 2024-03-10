const baseURL = 'api/v1'

const pictures = '/pictures'

const urls = {
    pictures: {
        base: pictures,
        byId:(id:string):string=>`${pictures}/${id}`
    }
}

export {
    baseURL,
    urls
}