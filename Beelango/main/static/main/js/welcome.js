function areYouRegistered(){
    let windowLogin = document.getElementById('auth')
    if (windowLogin.style.display === '') {
        document.body.style.pointerEvents = 'none'
        document.body.style.overflowY = 'hidden'
        document.body.style.userSelect = 'none'
        windowLogin.style.opacity = '0'
        windowLogin.style.display = 'block'
        windowLogin.style.pointerEvents = 'auto'
        windowLogin.style.transition = 'opacity 500ms'
        anim(0, 1)
    } else {
        windowLogin.style.transition = 'opacity 250ms'
        document.body.style.overflowY = 'scroll'
        document.body.style.pointerEvents = 'auto'
        document.body.style.userSelect = 'auto'
        anim(0, 0)
        anim(250, 0, 'none')
    }
    function anim(timeout, opacity = 0, mode = ''){
        setTimeout(() => {
            windowLogin.style.opacity = `${opacity}`
            if (mode === 'none') windowLogin.style.display = ''
        }, timeout)
    }
}

let flagg = 0

window.addEventListener("scroll", function (){
    let button = document.getElementById('welcome-start-button')
    let header = document.getElementById('header')
    let cancel = document.getElementById('cancel')
    let auth = document.getElementById('auth')
    let areYouRegistered = document.getElementById('are-you-registered')
    let login = document.getElementById('login')
    let register = document.getElementById('register')
    if (button.getBoundingClientRect().bottom < 0){
        if (flagg === 0){
            header.style.top = `-${header.getBoundingClientRect().height}px`
            header.style.transition = 'top 250ms'
            header.style.top = '0px'
            cancel.style.color = 'white'
            auth.style.background = '#3388DD'
            areYouRegistered.style.color = 'white'
            login.style.color = '#3388DD'
            login.style.background = 'white'
            register.style.color = '#3388DD'
            register.style.background = 'white'
        }
        flagg = 1
    } else {
        header.style.top = `-${header.getBoundingClientRect().height}px`
        cancel.style.color = '#3388DD'
        auth.style.background = 'white'
        areYouRegistered.style.color = '#3388DD'
        login.style.color = 'white'
        login.style.background = '#38D'
        register.style.color = 'white'
        register.style.background = '#38D'
        flagg = 0
    }
})