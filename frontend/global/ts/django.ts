export interface DJANGO {
    env: string, // see DJANGO_ENV
}


declare global {
    export interface Window {
        DJANGO: DJANGO;
    }
}
