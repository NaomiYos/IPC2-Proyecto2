async function CrearCliente() {
    let correo= document.getElementById('txtmail').value
    let pwd = document.getElementById('txtcontra').value
    let nombre= document.getElementById('txtnombre').value
    let apellido = document.getElementById('txtapellido').value
    let edad = document.getElementById('txtedad').value
    let dpi = document.getElementById('txtdpi').value
    let compras = document.getElementById('txtcompra').value

    // Peticion HTTP hacia nuestro backend
    let rawResponse = await fetch("http://localhost:3000/cliente", {
        
    method: "PUT",
        
        headers: {'Content-type': 'application/json'},
       
        body: JSON.stringify({

            "dpi": dpi,
            "nombre": nombre,
            "apellido":apellido,
            "correo": correo,
            "password": pwd,
            "edad": edad,
            "compras": compras

            }
        )
    })
    const response = await rawResponse.json()
    if(rawResponse.status == 201){
        console.log(response)
        alert(`Usuario creado  `)
        
    } else {
        alert(response.mensaje)
    }


    
}
async function Crearproducti() {
    let datos= document.getElementById('txtproductos')

    // Peticion HTTP hacia nuestro backend
    let rawResponse = await fetch("http://localhost:3000/cliente", {
        
    method: "PUT",
        
        headers: {'Content-type': 'application/json'},
       
        body: JSON.stringify({

            "dpi": datos,
            "nombre": datos,
            "apellido":datos,
            "correo": correo,
            "password": pwd,
            "edad": edad,
            "compras": compras

            }
        )
    })
    const response = await rawResponse.json()
    if(rawResponse.status == 201){
        console.log(response)
        alert(`Usuario creado  `)
        
    } else {
        alert(response.mensaje)
    }


    
}
async function CrearVenta() {
  
    let no= document.getElementById('txtno')
    let date= document.getElementById('txtfecha')
    let nombre=document.getElementById('txtnombre')
    let total=document.getElementById('txttotal')
    let dpi= document.getElementById('txtdpi')
    let prod= document.getElementById('txtproducto')

    // Peticion HTTP hacia nuestro backend
    let rawResponse = await fetch("http://localhost:3000/ventas", {
        
    method: "PUT",
        
        headers: {'Content-type': 'application/json'},
       
        body: JSON.stringify({
            "no": 100,
            "fecha": date,
            "dpi_cliente":dpi ,
            "nombre_cliente": "Allan",
            "producto": prod,
            "total":total

            }
        )
    })
    const response = await rawResponse.json()
    if(rawResponse.status == 201){
        console.log(response)
        alert(`Usuario creado  `)
        
    } else {
        alert(response.mensaje)
    }


    
}