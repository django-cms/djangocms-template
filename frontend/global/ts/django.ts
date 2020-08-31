export interface django {
    env: string, // see settings.DJANGO_ENV
}


declare global {
    export interface Window {
        django: django;
    }
}
