async function iniciarSesion() {
    let correo = document.getElementById('txtmail').value
    let pwd = document.getElementById('txtpass').value

    // Peticion HTTP hacia nuestro backend
    let rawResponse = await fetch("http://localhost:3000/authA", {
        
    method: "POST",
        
        headers: {'Content-type': 'application/json'},
       
        body: JSON.stringify({
            
                "correo": correo,
                "password": pwd
            }
        )
    })
    const response = await rawResponse.json()
    if(rawResponse.status == 200){
        console.log(response)
        alert(`Bienvenid@  `)
        localStorage.setItem("correo", JSON.stringify(response))
        window.open('home.html', '_self'); 
    } else {
        alert(response.mensaje)
    }

    let usuarioRecuperado = localStorage.getItem("correo")
    
    console.log(usuarioRecuperado)
    
    if(usuarioRecuperado){
        usuarioRecuperado = await JSON.parse(usuarioRecuperado)
    }

    console.log(usuarioRecuperado)
    
}
async function iniciarSesionC() {
    let correo = document.getElementById('txtcorreo').value
    let pwd = document.getElementById('txtpass').value

    // Peticion HTTP hacia nuestro backend
    let rawResponse = await fetch("http://localhost:3000/auth", {
        
    method: "POST",
        
        headers: {'Content-type': 'application/json'},
       
        body: JSON.stringify({
            
                "correo": correo,
                "password": pwd
            }
        )
    })
    const response = await rawResponse.json()
    if(rawResponse.status == 200){
        console.log(response)
        alert(`Bienvenid@  `)
        localStorage.setItem("correo", JSON.stringify(response))
        window.open('home.html', '_self'); 
    } else {
        alert(response.mensaje)
    }

    let usuarioRecuperado = localStorage.getItem("correo")
    
    console.log(usuarioRecuperado)
    
    if(usuarioRecuperado){
        usuarioRecuperado = await JSON.parse(usuarioRecuperado)
    }

    console.log(usuarioRecuperado)
    
}
async function CrearUsuarioC() {
    let correoC = document.getElementById('txtcor').value
    let pwdC = document.getElementById('txtcontra').value
    let nombre= document.getElementById('txtnombre').value
    let apellido = document.getElementById('txtapellido').value
    let edad = document.getElementById('txtedad').value
    let dpi = document.getElementById('txtdpi').value

    // Peticion HTTP hacia nuestro backend
    let rawResponse = await fetch("http://localhost:3000/cliente", {
        
    method: "PUT",
        
        headers: {'Content-type': 'application/json'},
       
        body: JSON.stringify({

            "dpi": dpi,
            "nombre": nombre,
            "apellido":apellido,
            "correo": correoC,
            "password": pwdC,
            "edad": edad,
            "compras": 0

            }
        )
    })
    const response = await rawResponse.json()
    if(rawResponse.status == 201){
        console.log(response)
        alert(`Usuario $(response.data.nombre})  `)
        
    } else {
        alert(response.mensaje)
    }


    
}

