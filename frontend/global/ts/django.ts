export interface DJANGO {
    env: string, // see settings.DJANGO_ENV
}


declare global {
    export interface Window {
        DJANGO: DJANGO;
    }
}
