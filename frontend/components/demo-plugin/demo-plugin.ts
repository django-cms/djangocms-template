document.addEventListener('DOMContentLoaded', () => {
    demoPluginInit();
});

function demoPluginInit() {
    document.removeEventListener('DOMContentLoaded', attachListenersToDOM);
    document.addEventListener('DOMContentLoaded', attachListenersToDOM);
}

function attachListenersToDOM() {
}
